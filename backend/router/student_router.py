from fastapi import APIRouter
from ..schema.student_schema import StudentModel
from ..service.student_service import register_student

router = APIRouter()

@router.post('/register')
async def register(student: StudentModel):
	return register_student(student)