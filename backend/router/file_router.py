from fastapi import APIRouter, UploadFile, File
from ..service.file_service import upload_file, download_file

router = APIRouter()

@router.post("/file")
async def post_file(file: UploadFile = File(...)):
	return await upload_file(file)

@router.get("/file")
async def get_file(file_name: str):
	return await download_file(file_name)