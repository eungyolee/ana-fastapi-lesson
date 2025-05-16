from fastapi import APIRouter, Path, Header, HTTPException
from ..service.password_service import check_password

router = APIRouter()

@router.get("/auth/{password}")
async def auth_password(
	password: str = Path(
		...,
		min_length=4,
		max_length=15,
		regex="^[a-zA-Z0-9]+$"
	),
	secret_token: str = Header(...)
):
	if secret_token is None or secret_token != "QWERTY":
		raise HTTPException(status_code=401, detail="Invalid Token")

	result = check_password(password)

	if not result:
		raise HTTPException(status_code=401, detail="Wrong Password")
	return result