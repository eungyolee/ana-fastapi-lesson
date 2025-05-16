from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .router import router as api_router
from .utils.exceptions import ValidationException

app = FastAPI(
	title="250516 AnA 실습",
	description="아 하기 싫다 집가고 싶다",
	version="1.0.0"
)

app.include_router(api_router)

@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exc: ValidationException):
	return JSONResponse(
		status_code=451,
		content={
			"message": "검증에 실패했습니다. FBI OPEN UP NORHU1130",
			"detail": str(exc)
		}
	)