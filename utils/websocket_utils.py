from fastapi import WebSocket

class ConnectionManager():
    def __init__(self):
        self.active_conn: list[WebSocket] = []
        
    async def connect(self,web_socket:WebSocket):
        await web_socket.accept()
        self.active_conn.append(web_socket)
        
    def disconnect(self,web_socket:WebSocket):
        self.active_conn.remove(web_socket)
        
    async def send_a_message(self,message:str, web_socket:WebSocket):
        await web_socket.send_text(message)
        
    async def broadcast_message(self, message:str):
        for conn in self.active_conn:
            await conn.send_text(message)
