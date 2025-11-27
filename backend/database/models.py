from sqlalchemy import Column, Integer, Text, DateTime, func
from .db import Base

class CodeSnippet(Base):
    __tablename__ = "code_snippets"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Text, nullable=False)
    ai_suggestion = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())