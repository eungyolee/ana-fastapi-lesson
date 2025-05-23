from fastapi import APIRouter
from .password_router import router as password_router
from .student_router import router as student_router
from .file_router import router as file_router

router = APIRouter()

router.include_router(password_router, tags=["250516"])
router.include_router(student_router, tags=["250516"])
router.include_router(file_router, tags=["250523"])