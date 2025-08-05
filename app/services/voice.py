import httpx, structlog, anyio
from app.core.config import get_settings
settings, log = get_settings(), structlog.get_logger()
async def synthesize(text: str) -> str:
    headers = {'xi-api-key': settings.ELEVENLABS_API_KEY or ''}
    async with httpx.AsyncClient(timeout=60) as c:
        r = await c.post(f'{settings.VOICE_URL}/v1/tts', json={'text':text}, headers=headers); r.raise_for_status()
        return r.json()['audio_url']
def synthesize_sync(text: str) -> str:
    return anyio.run(synthesize, text)
