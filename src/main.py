import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from src.controllers import ds4_model_api
from config.settings import Setting


settings = Setting()

src = FastAPI(
    title="tac-api",
    description="TAC medication categorization prediction",
    version=settings.VERSION,
    root_path=settings.ROOT_PATH,
    redoc_url=None,
)

src.include_router(ds4_model_api.ds4_model_api)

src.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS,
)

@src.get("/")
async def root():
    return RedirectResponse("/docs/")


if __name__ == "__main__":
    uvicorn.run(src, host="0.0.0.0", port=8000)
