from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .router import router as api_router
from .utils.exceptions import ValidationException, LoginFailedException
from .middleware import middlewares

app = FastAPI(
	title="AnA FastAPI 실습",
	description="아 하기 싫다 집가고 싶다",
	version="1.0.0"
)

for middleware in middlewares:
	app.middleware("http")(middleware)

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

@app.exception_handler(LoginFailedException)
async def login_failed_exception_handler(request: Request, exc: LoginFailedException):
	return JSONResponse(
		status_code=401,
		content={
			"message": "비밀번호 틀림",
			"detail": str(exc)
		}
	)