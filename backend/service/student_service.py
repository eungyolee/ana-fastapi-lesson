from ..schema.student_schema import StudentModel

def register_student(student: StudentModel):
	return {
		"name": student.name,
		"student_id": str(student.student_id),
		"department": student.department,
		"grade": str(student.grade),
		"club": student.club
	}