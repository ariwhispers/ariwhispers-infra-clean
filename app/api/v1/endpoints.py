import structlog
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.config import get_settings
from app.services import queue
from app.api.v1.schemas import PromptIn, GenerateOut
log = structlog.get_logger()
router = APIRouter()
@router.get('/health', tags=['meta'])
async def health() -> dict[str,str]:
    return {'status':'ok'}
@router.post('/generate', response_model=GenerateOut, tags=['generate'])
async def generate(prompt: PromptIn, settings=Depends(get_settings)) -> GenerateOut:
    try:
        task_id = await queue.enqueue_generate(prompt.text)
        return GenerateOut(reply='🕐 Generating …', image_url=None, audio_url=None)
    except Exception as exc:
        log.error('generate-failed', err=str(exc))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='generation failed')
