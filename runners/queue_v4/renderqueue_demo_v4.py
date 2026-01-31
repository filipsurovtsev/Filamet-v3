from core.render.queue_v4 import RenderQueueV4

def main():
    q = RenderQueueV4(max_concurrent=2)

    for i in range(5):
        q.enqueue(f"job_{i+1}")

    print("INITIAL_STATS", q.stats())

    started = []
    while q.can_start():
        jid = q.start_next()
        if jid:
            started.append(jid)
    print("AFTER_FIRST_START", q.stats())

    if started:
        q.finish(started[0])
    print("AFTER_FINISH_ONE", q.stats())

    while q.can_start():
        jid = q.start_next()
        if jid:
            started.append(jid)
    print("AFTER_SECOND_START", q.stats())

if __name__ == "__main__":
    main()
