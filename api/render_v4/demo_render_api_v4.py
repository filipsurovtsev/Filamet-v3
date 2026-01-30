from api.render_v4.render_api_v4 import handle_render_request_v4

req = {"job_id": "demo_api_v4", "payload": {"demo": True}}
res = handle_render_request_v4(req)
print("RENDER_API_V4_DEMO_OK", res)
