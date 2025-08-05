from celery import Celery
import structlog
from app.core.config import get_settings
settings = get_settings()
celery = Celery(__name__, broker=settings.REDIS_URL, backend=settings.REDIS_URL)
celery.conf.task_routes = {'app.tasks.*': {'queue': 'ariwhispers'}}
log = structlog.get_logger()
async def enqueue_generate(prompt: str) -> str:
    task = celery.send_task('app.tasks.generate_full', args=[prompt])
    log.info('task-enqueued', task_id=task.id)
    return task.id
