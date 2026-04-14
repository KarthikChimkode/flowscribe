import httpx 
from .base import LLMProvider
from config.config import settings

class GeminiProvider(LLMProvider):
    def __init__(self):
        # Gemini uses a special URL that includes your API key 
    self.api_key = settings.GEMINI_API_KEY
    self.url=f"https://gemerativelangugae.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.api_key}"

    async def generate(self, prompt: str) -> str:
        # The data format for Gemini is a bit different than Ollama
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(self.url, json=payload, timeout=60.0)
            response.raise_for_status()

            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']