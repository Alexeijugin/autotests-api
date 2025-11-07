import asyncio

import websockets

async def client():
    uri = "ws://localhost:8765"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        await websocket.send(f'Привет сервер')

        for _ in range(5):
            response = await websocket.recv()  # Получаем ответ от сервера
            print(f"Ответ от сервера: {response}")


asyncio.run(client())