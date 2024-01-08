from fastapi import FastAPI
from fastapi.responses import JSONResponse
from lagom.integrations.fast_api import FastApiIntegration

from src.services import ScrapperService
from src.infraestructure import CustomError
from src.infraestructure.Container import container as MyContainer

app = FastAPI()
deps= FastApiIntegration(MyContainer)

@app.get('/')
async def index(service=deps.depends(ScrapperService)):
    return service.process()

@app.exception_handler(CustomError)
async def custom_exception_handler(request, exception:CustomError):
    return JSONResponse(
        content={"error_code":exception.error_code, "message":exception.message},
        status_code=exception.status_code
    )