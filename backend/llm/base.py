from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod 
    async def generate(self, prompt: str) -> str:
        """
        ALL AI providers must implement this method. 
        It takes a prompt (text) and returns a suggestion (text).
        """
        pass 

        