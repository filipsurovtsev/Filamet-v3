from api.render_v4.render_api_v4 import handle_render_request_v4

res = handle_render_request_v4({"job_id": "smoke_api_v4"})
print("RENDER_API_V4_SMOKE_OK", res)
