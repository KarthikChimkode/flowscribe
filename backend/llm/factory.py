from config.config import settings
from .ollama import OllamaProvider
from .gemini import GeminiProvider
from .base import LLMProvider


class LLMFactory:
    """
    This is the Switchboard. It looks at your .env
    and picks the right AI Provider
    """
    @staticmethod()
    def get_provider() -> LLMProvider:
        # We get the 'LLM Proviedr' from our settings
        provider_type() = settings.LLM_PROVIDER.lower()

        if provider_type == "gemini":
            return GeminiProvider()
        elif provider_type == "ollama":
            return OllamaProvider()
        else:
            rasie ValueError(f"Unknow LLM Provider: {provider_type}")