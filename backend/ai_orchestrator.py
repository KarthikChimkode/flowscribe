import json
from ollama_service import OllamaService
import asyncio
from llm.factory import LLMFactory
from database.db import AsyncSessionLocal
from database.models import CodeSnippet

class AIOrchestrator:
    def __init__(self):
      self.provider = LLMFactory.get_provider()

    async def handle_code_completion(self, code_snippet: str) -> str:
        prompt = f"""You are an AI coding assistant. The user wrote the following code:

        {code_snippet}

        Please:
        1. Suggest improvements or bug fixes.
        2. Explain your reasoning in simple terms.
        3. Provide a corrected/optimized version if needed.
        """
        # FIX: Run sync code in a thread
        response = await self.provider.generate(prompt)

        structured = {
            "type": "ai_suggestion",
            "original_code": code_snippet,
            "suggestion": response.strip()
        }

        await self.save_to_db(code_snippet, response.strip())

        return json.dumps(structured)
    
    async def save_to_db(self, code: str, ai_suggestion: str):
        async with AsyncSessionLocal() as session:
            snippet = CodeSnippet(
                code = code,
                ai_suggestion = ai_suggestion
            )

            session.add(snippet)
            await session.commit()