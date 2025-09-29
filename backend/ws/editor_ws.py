# ws/editor_ws.py
from fastapi import WebSocket
import json
import asyncio
from ai_orchestrator import AIOrchestrator

orchestrator = AIOrchestrator()

async def editor_websocket(websocket: WebSocket, redis_client):
    await websocket.accept()
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("flow:editor")

    async def read_from_ws():
        """Task A: Read events from the editor (user actions) and publish to redis"""
        try:
            while True:
                raw = await websocket.receive_text()
                event = json.loads(raw)

                print("User event:", event)

                # Publish event to Redis (so others see it)
                await redis_client.publish("flow:editor", json.dumps(event))

                if event.get("event") == "insert":
                    suggestion = await orchestrator.handle_code_completion(event["text"])
                    await websocket.send_text(suggestion)

        except Exception:
            await pubsub.unsubscribe("flow:editor")


    async def read_from_redis():
        """Task B: Listen to redis channel and forward events to the editor"""
        try:
            async for msg in pubsub.listen():
                if msg["type"] == "message":
                    event = json.loads(msg["data"])
                    await websocket.send_text(json.dumps(event))
        except Exception:
            await pubsub.unsubscribe("flow:editor")

    # Run both tasks concurrently
    await asyncio.gather(read_from_ws(), read_from_redis())
