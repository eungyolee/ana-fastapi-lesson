from fastapi import Request
import time

async def request_time_middleware(request: Request, call_next):
	start_time = time.time()

	response = await call_next(request)

	end_time = time.time()
	duration = end_time - start_time

	# print(f"요청 처리 시간 : {duration:.6f}초")
	response.headers["X-Request-Time"] = str(duration)

	return response