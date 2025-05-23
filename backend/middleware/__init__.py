from .request_time import request_time_middleware
from .check_path import check_path_middleware

middlewares = [
	check_path_middleware,
	request_time_middleware
]