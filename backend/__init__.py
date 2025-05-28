from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .router import router as api_router
from .utils.exceptions import ValidationException, LoginFailedException
from .middleware import middlewares

app = FastAPI(
	title="AnA FastAPI 실습",
	description="노현우 죽인다",
	version="1.0.0"
)

for middleware in middlewares:
	app.middleware("http")(middleware)

origins = [
	'http://localhost:3000',
	'https://naver.com',
	'https://eungyolee.kr'
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,  # 허용할 출처 -> origins
	allow_credentials=True,  # 자격 증명 허용 여부 -> 참
	allow_methods=["*"],  # 허용할 메서드 -> 전부
	allow_headers=["*"]  # 허용할 헤더 -> 전부
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

@app.exception_handler(LoginFailedException)
async def login_failed_exception_handler(request: Request, exc: LoginFailedException):
	return JSONResponse(
		status_code=401,
		content={
			"message": "비밀번호 틀림",
			"detail": str(exc)
		}
	)