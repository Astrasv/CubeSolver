from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.config import settings
from app.routers import router as solve_router

app = FastAPI(title=settings.app_title)

app.include_router(solve_router, prefix=settings.api_prefix)


@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )
