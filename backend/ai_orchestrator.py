import json
from ollama_service import OllamaService
import asyncio

class AIOrchestrator:
    def __init__(self, model: str = "codellama:7b"):
        self.client = OllamaService()
        self.model = model

    async def handle_code_completion(self, code_snippet: str) -> str:
        prompt = f"""You are an AI coding assistant. The user wrote the following code:

        {code_snippet}

        Please:
        1. Suggest improvements or bug fixes.
        2. Explain your reasoning in simple terms.
        3. Provide a corrected/optimized version if needed.
        """
        # FIX: Run sync code in a thread
        response = await asyncio.to_thread(
            self.client.generate, self.model, prompt
        )

        structured = {
            "type": "ai_suggestion",
            "original_code": code_snippet,
            "suggestion": response.strip()
        }

        return json.dumps(structured)