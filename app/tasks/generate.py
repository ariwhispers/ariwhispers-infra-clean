import structlog
from celery import shared_task
from app.services import llm, images, voice
log = structlog.get_logger()
@shared_task(name='app.tasks.generate_full')
def generate_full(prompt: str) -> dict:
    reply = llm.chat_sync(prompt)
    image_url = images.generate_img_sync(reply)
    audio_url = voice.synthesize_sync(reply)
    return {'reply': reply, 'image_url': image_url, 'audio_url': audio_url}
