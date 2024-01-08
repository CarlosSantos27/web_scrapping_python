from fastapi import HTTPException

class CustomError(HTTPException):
    def __init__(self, error_code, message, status_code):
        self.error_code = error_code
        self.message = message
        self.status_code = status_code
        super().__init__(status_code=status_code,detail=message)