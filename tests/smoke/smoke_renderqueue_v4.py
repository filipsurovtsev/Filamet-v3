from core.render.queue_v4 import RenderQueueV4

def run_smoke():
    q = RenderQueueV4(max_concurrent=1)

    q.enqueue("job_a")
    q.enqueue("job_b")

    j1 = q.start_next()
    assert j1 == "job_a"
    assert not q.can_start()

    q.finish(j1)
    assert q.can_start()

    j2 = q.start_next()
    assert j2 == "job_b"
    q.finish(j2)

    stats = q.stats()
    assert stats["pending"] == []
    assert stats["running"] == []

    return {"status": "ok", "stats": stats}

if __name__ == "__main__":
    res = run_smoke()
    print("RENDERQUEUE_V4_SMOKE_OK", res)
