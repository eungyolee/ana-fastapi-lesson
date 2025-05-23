from .request_time import request_time_middleware
# from .check_path import check_path_middleware
from .logging import logging_middleware

middlewares = [
	request_time_middleware,
	logging_middleware
]