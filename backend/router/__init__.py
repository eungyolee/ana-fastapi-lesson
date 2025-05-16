from fastapi import APIRouter
from .password_router import router as password_router
from .student_router import router as student_router

router = APIRouter()

router.include_router(password_router)
router.include_router(student_router)