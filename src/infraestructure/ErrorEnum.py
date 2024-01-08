from enum import Enum
from fastapi import status
from .custom_error import CustomError

class ErrorCode(str,Enum):
    E001 = "E001"
    E002 = "E002"
    E003 = "E003"
        
ERRORS = {
    ErrorCode.E001: CustomError(ErrorCode.E001, "Server internal error", status.HTTP_500_INTERNAL_SERVER_ERROR),
    ErrorCode.E002: CustomError(ErrorCode.E002, "Google has detected automated queries", status.HTTP_423_LOCKED),
    ErrorCode.E003: CustomError(ErrorCode.E003, "Driver web not defined", status.HTTP_422_UNPROCESSABLE_ENTITY),
}