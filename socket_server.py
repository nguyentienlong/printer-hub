import asyncio
import json
import os
import websockets

async def print(websocket, path):
    data = await websocket.recv()

    data_in_dict = json.loads(data)

    os.system('python print_handler.py "{}"'.format(data_in_dict))

    await websocket.send(data)


start_server = websockets.serve(print, "127.0.0.1", 2377)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()