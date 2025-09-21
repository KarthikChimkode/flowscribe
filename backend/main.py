from fastapi import FastAPI, WebSocket
import uvicorn
import redis.asyncio as redis
import asyncio
import json


app = FastAPI(title="FlowScribe")


@app.on_event("startup")
async def startup_event():
    app.state.redis = await redis.from_url(
        "redis://localhost:6379", decode_responses=True
    )


@app.on_event("shutdown")
async def shutdown_event():
    await app.state.redis.close()

@app.websocket("/ws/editor")
async def editor_websocket(websocket: WebSocket):
    await websocket.accept()

    redis_client = app.state.redis
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("flow:editor")

    async def read_from_ws():
        """Task A: Read events from the editor (user actions) and publish to redis"""

        try:
            while True:
                raw = await websocket.receive_text()
                event = json.loads(raw)

                # Example :{"event": "insert", "position": 42, "text":"print("}
                print("User event:", event)

                await redis_client.publish("flow:editor", json.dumps(event))
        except Exception:
            await pubsub.unsubscribe("flow:editor")
        
    async def read_from_redis():
        """Task B: Listen to redis channel and forward events to the editor"""

        try:
            async for msg in pubsub.listen():
                if msg["type"] == "message":
                    event = json.loads(msg["data"])
                
                    # Example: {"event": "suggestion", "position": 42, "text": "print('Hello, world!')"}
                    await websocket.send_text(json.dumps(event))
        except Exception:
            await pubsub.unsubscribe("flow:editor")
        
    await asyncio.gather(read_from_ws(), read_from_redis())
