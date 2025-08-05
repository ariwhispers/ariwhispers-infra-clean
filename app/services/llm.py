import httpx, structlog, anyio
from app.core.config import get_settings
settings, log = get_settings(), structlog.get_logger()
async def chat(prompt: str) -> str:
    async with httpx.AsyncClient(timeout=60) as c:
        r = await c.post(f'{settings.LLM_URL}/v1/chat', json={'prompt':prompt}); r.raise_for_status()
        return r.json()['reply']
def chat_sync(prompt: str) -> str:
    return anyio.run(chat, prompt)
