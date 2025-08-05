import httpx, structlog, anyio
from app.core.config import get_settings
settings, log = get_settings(), structlog.get_logger()
async def generate_img(prompt: str) -> str:
    async with httpx.AsyncClient(timeout=120) as c:
        r = await c.post(f'{settings.IMG_URL}/generate', json={'prompt':prompt}); r.raise_for_status()
        return r.json()['url']
def generate_img_sync(prompt: str) -> str:
    return anyio.run(generate_img, prompt)
