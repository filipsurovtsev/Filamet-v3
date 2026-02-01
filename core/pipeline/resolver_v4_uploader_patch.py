from core.pipeline.workers.uploader_v4 import UploaderV4
def register(p):
    p["UPLOAD_V4"] = UploaderV4
