# see https://aiohttp.readthedocs.io
import asyncio
import aiohttp
from aiohttp import web

async def handle(request):
    name=request.match_info.get('name',"Anonymous")
    text = "Hello, "+ name
    return web.Response(text=text)

async def websocket_handler(request):

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws

print("Start Web App")
app = web.Application()
app.add_routes([web.get('/',handle),
                web.get('/ws', websocket_handler),
                web.get('/{name}',handle)])
web.run_app(app)

