class ValidationException(Exception):
	def __init__(self, message: str):
		super().__init__(message)

class LoginFailedException(Exception):
	def __init__(self, message: str):
		super().__init__(message)