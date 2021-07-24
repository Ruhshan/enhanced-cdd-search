from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from backend.core.config import settings
from backend.exception.custom_exception_handler import include_custom_exception_handler
from backend.routers import search_router
from backend.service.async_http_client import AIOClient

app = FastAPI()

app = FastAPI(
    title=settings.PROJECT_NAME)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(search_router.router,prefix=settings.API_V1_STR+"/search")
include_custom_exception_handler(app)

@app.on_event('startup')
async def startup_event():
    await AIOClient.create_session()

@app.on_event('shutdown')
async def shutdown_event():
    await AIOClient.close_session()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8090)