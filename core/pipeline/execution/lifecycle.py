from core.utils.log import log

def lifecycle_run(task):
    log(f"task {task.__class__.__name__}: prepare")
    task.prepare()
    log(f"task {task.__class__.__name__}: execute")
    task.execute()
    log(f"task {task.__class__.__name__}: finalize")
    task.finalize()
    return {"status": "OK"}
