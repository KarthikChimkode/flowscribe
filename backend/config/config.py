import os 
from dotenv import load_dotenv

# This tells python to stay at the current folder and look for the .env file
load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")


    # LLM Settings
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "ollama")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "codellama:7b")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")


#we create one "settings" object that we can use everywhere in our app
settings = Settings()