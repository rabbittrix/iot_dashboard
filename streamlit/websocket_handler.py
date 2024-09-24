import asyncio
import websockets
import threading

async def handler(websocket):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send("Message received")

def start_websocket_server():
    start_server = websockets.serve(handler, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

def init_websocket():
    # Start the WebSocket server in a new thread
    thread = threading.Thread(target=start_websocket_server)
    thread.daemon = True  # This allows the thread to exit when the main program exits
    thread.start()
