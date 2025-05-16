from fastapi import APIRouter, Path
from ..service.password_service import check_password

router = APIRouter()

@router.get("/auth/{password}")
async def auth_password(
	password: str = Path(
		...,
		min_length=4,
		max_length=15,
		regex="^[a-zA-Z0-9]+$"
	)
):
	return check_password(password)