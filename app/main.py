from contextlib import asynccontextmanager
import structlog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.core.logging import setup_logging
from app.api.v1.endpoints import router as v1_router
settings = get_settings()
setup_logging(settings.LOG_LEVEL)
log = structlog.get_logger()
@asynccontextmanager
async def lifespan(_: FastAPI):
    log.info('startup', env=settings.ENV); yield; log.info('shutdown')
app = FastAPI(title='AriWhispers Backend', version='1.0.0', lifespan=lifespan, docs_url='/')
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
app.include_router(v1_router, prefix='/api/v1')
