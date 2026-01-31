from runners.queue_v4.renderqueue_daemon_v4 import RenderQueueDaemonV4, queue

queue.enqueue("job_demo_1")
queue.enqueue("job_demo_2")

daemon = RenderQueueDaemonV4(queue, interval=0.0)
stats = daemon.run(steps=5)

print("RENDERQUEUE_DAEMON_V4_SMOKE_OK", stats)
