from fastapi import UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import shutil

ALLOWED_EXTENSIONS = {'txt', 'jpg', 'png'}

async def upload_file(file: UploadFile = File(...)):
	if not file.filename.endswith(tuple(ALLOWED_EXTENSIONS)):
		raise HTTPException(status_code=400, detail="확장자 틀림")

	save_path = f"uploaded_files/{file.filename}"

	with open(save_path, "wb") as buffer:
		shutil.copyfileobj(file.file, buffer)

	return {
		"filename": file.filename,
		"content_type": file.content_type,
		"size": file.size,
		"save_path": save_path
	}

async def download_file(file_name: str):
	return FileResponse(
		f"uploaded_files/{file_name}",
		media_type='application/octet-stream',
		filename=file_name
	)