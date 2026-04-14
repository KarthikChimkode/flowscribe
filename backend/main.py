from fastapi import FastAPI, WebSocket
import redis.asyncio as redis
from ws.editor_ws import editor_websocket
from fastapi import FastAPI
from database.init_db import init_db
from config.config import settings

app = FastAPI(title="FlowScribe")

@app.on_event("startup")
async def startup_event():
    app.state.redis = await redis.from_url(settings.REDIS_URL, decode_responses=True)

@app.on_event("shutdown")
async def shutdown_event():
    await app.state.redis.close()

@app.websocket("/ws/editor")
async def editor_ws(websocket: WebSocket):
    await editor_websocket(websocket, app.state.redis)

@app.on_event("startup")
async def startup():
    await init_db()