from core.pipeline.router import route_job

print("ROUTER_V4_SMOKE:",
      route_job({
          "type": "VK_POST_V4",
          "job_id": "test_router",
          "payload": {"text": "router test"}
      }))
