import os
from typing import Any, Dict, Optional

from core.pipeline.tasks.base import BaseTask
from core.context.task_context import TaskContext
from core.context.media_context import MediaContext
from core.media.io.errors import MediaFileNotFoundError, MediaProbeError, UnsafeMediaAccessError

try:
    import whisper  # requires `pip install openai-whisper`
except ImportError:
    whisper = None


def _get_job_id(context: TaskContext) -> str:
    job = getattr(context, "job", None)
    if job is not None:
        return getattr(job, "id", None) or getattr(job, "job_id", "unknown_job")
    return getattr(context, "job_id", "unknown_job")


def _ensure_output_dir(job_id: str) -> str:
    base_dir = os.path.join("output", "transcripts", job_id)
    os.makedirs(base_dir, exist_ok=True)
    return base_dir


def _run_whisper_transcribe(path: str, model_name: str = "small") -> str:
    if whisper is None:
        raise RuntimeError("whisper package is not installed; install with `pip install openai-whisper`")
    model = whisper.load_model(model_name)
    result: Dict[str, Any] = model.transcribe(path)
    text = result.get("text") or ""
    return text.strip()


class TranscribeTask(BaseTask):
    task_type = "TRANSCRIBE"

    def run(self, context: TaskContext, logger: Optional[Any] = None) -> Dict[str, Any]:
        media_ctx: MediaContext = getattr(context, "media", None)
        if media_ctx is None or media_ctx.descriptor is None:
            raise RuntimeError("TranscribeTask: media context or descriptor is missing")

        if not media_ctx.is_safe():
            if logger and hasattr(logger, "error"):
                logger.error("TranscribeTask: media descriptor is not marked safe")
            raise UnsafeMediaAccessError("unsafe media descriptor")

        if not media_ctx.probe_media(logger=logger):
            raise RuntimeError(f"TranscribeTask: probe failed: {media_ctx.probe_error}")

        media_path = media_ctx.descriptor.path
        if logger and hasattr(logger, "info"):
            logger.info(f"TranscribeTask: starting transcription for {media_path}")

        try:
            raw_text = _run_whisper_transcribe(media_path)
        except (MediaFileNotFoundError, MediaProbeError, UnsafeMediaAccessError) as exc:
            if logger and hasattr(logger, "error"):
                logger.error(f"TranscribeTask: media safety/IO error: {exc}")
            raise
        except Exception as exc:  # noqa: BLE001
            if logger and hasattr(logger, "exception"):
                logger.exception(f"TranscribeTask: transcription failed: {exc}")
            raise

        job_id = _get_job_id(context)
        out_dir = _ensure_output_dir(job_id)
        out_path = os.path.join(out_dir, "raw_transcript.txt")

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(raw_text)

        job = getattr(context, "job", None)
        if job is not None:
            output = getattr(job, "output", None)
            if output is None:
                output = {}
                setattr(job, "output", output)
            if isinstance(output, dict):
                transcripts_info = output.get("transcripts") or {}
                transcripts_info.update(
                    {
                        "raw_path": out_path,
                        "length_chars": len(raw_text),
                    }
                )
                output["transcripts"] = transcripts_info

        if logger and hasattr(logger, "info"):
            logger.info(f"TranscribeTask: transcript saved to {out_path} ({len(raw_text)} chars)")

        return {
            "status": "OK",
            "job_id": job_id,
            "transcript_path": out_path,
            "length_chars": len(raw_text),
        }
