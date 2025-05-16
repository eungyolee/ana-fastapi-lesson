from fastapi import APIRouter, Header, HTTPException
from ..schema.student_schema import StudentModel
from ..service.student_service import register_student
from ..utils.digits_sum import find_digits_sum
from ..utils.exceptions import ValidationException

router = APIRouter()

@router.post('/register')
async def register(
	student: StudentModel,
	validation_code: int = Header(...)
):
	if find_digits_sum(student.student_id * student.grade) != validation_code:
		# return "검증 코드가 잘못되었습니다."
		# raise HTTPException(status_code=400, detail="검증 코드가 잘못되었습니다.")
		raise ValidationException("검증 코드가 잘못되었습니다. aasdsdsasfd")
	return register_student(student)