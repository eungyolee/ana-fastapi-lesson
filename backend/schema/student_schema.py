from pydantic import BaseModel

class StudentModel(BaseModel):
	name: str
	student_id: int
	department: str
	grade: int
	club: str