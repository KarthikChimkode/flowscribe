import asyncio
import websockets
import json

async def test_editor_ws():
    uri = "ws://localhost:8000/ws/editor"
    async with websockets.connect(uri) as websocket:
        # Send a fake insert event
        event = {"event": "insert", "position": 0, "text": "print("}
        await websocket.send(json.dumps(event))
        print("Sent insert event:", event)

        # Wait for AI suggestion
        while True:
            response = await websocket.recv()
            try:
                msg = json.loads(response)
            except json.JSONDecodeError:
                msg = response  # Could be plain string
            print("Received:", msg)

            # Stop after receiving AI suggestion
            if isinstance(msg, dict) and msg.get("type") == "ai_suggestion":
                print("✅ AI suggestion received!")
                break


asyncio.run(test_editor_ws())
