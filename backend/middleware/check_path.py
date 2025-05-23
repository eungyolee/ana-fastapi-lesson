from fastapi import Request
from fastapi.responses import JSONResponse

async def check_path_middleware(request: Request, call_next):
	path = request.url.path

	if path == "/file":
		return JSONResponse(
			status_code=403,
			content={
				"detail": "경로 사용 불가"
			}
		)
	
	response = await call_next(request)
	return response