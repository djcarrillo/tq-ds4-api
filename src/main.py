import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from controllers import empowerment
from config.settings import Setting


settings = Setting()

src = FastAPI(
    title="tac-api",
    description="TAC categorization of a drug",
    version=settings.VERSION,
    root_path=settings.ROOT_PATH,
    redoc_url=None,
)

src.include_router(empowerment.empowerment_router)

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


#@src.get("/jobs/openapi.json", include_in_schema=False)
#async def root():
#    return RedirectResponse("/openapi.json")

if __name__ == "__main__":
    uvicorn.run(src, host="0.0.0.0", port=8000)
