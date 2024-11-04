from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from starlette.responses import FileResponse

from utils.websocket_utils import ConnectionManager

app = FastAPI()

@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.websocket("/ws/{client_id}")
async def websocket(web_socket: WebSocket, client_id: int):
    manager = ConnectionManager()
    await manager.connect(web_socket)
    try:
        while True:
            data = await web_socket.receive_text()
            await manager.send_a_message(f"you wrote {data}",web_socket)
            await manager.broadcast_message(f"Client {client_id} says {data}")
    except WebSocketDisconnect:
        manager.disconnect(web_socket)
        await manager.broadcast_message(f"Client {client_id} has left the chat!")
    
    