import time
from core.jobs.jobstore import JOBSTORE, update_status
from core.jobs.jobrouter import read_job
from core.utils.safe import safe_run
from core.utils.log import log

def worker_loop_v0():
    while True:
        log("heartbeat: worker_v0 alive")
        for job_id, job in list(JOBSTORE.items()):
            if job["status"] == "PENDING":
                update_status(job_id, "RUNNING")
                result = safe_run(lambda: "noop")
                if isinstance(result, dict) and "error" in result:
                    update_status(job_id, "FAILED")
                    log(f"job {job_id} failed")
                else:
                    update_status(job_id, "DONE")
                    log(f"job {job_id} done")
        time.sleep(1)

if __name__ == "__main__":
    worker_loop_v0()
