import httpx
from .base import LLMProvider
from config.config import settings

class OllamaProvider(LLMProvider):
    def __init__(self):
        self.url = settings.OLLAMA_URL
        self.model = settings.OLLAMA_MODEL

    async def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

    # We use httpx.AsyncClient() because it's fast and doesn't block other tasks
        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, json = payload, timeout=60.0)
            response.raise_for_status()
            return response.json().get("response", "")