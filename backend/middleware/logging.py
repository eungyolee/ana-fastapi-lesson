from fastapi import Request

async def logging_middleware(request: Request, call_next):
	request_method = request.method
	request_path = request.url.path

	print(f"{request_method} {request_path}")

	response = await call_next(request)

	response_status_code = response.status_code
	print(f"HTTP 상태 코드 : {response_status_code}")

	return response