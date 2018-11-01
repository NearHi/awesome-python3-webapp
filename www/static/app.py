#!usr/bin/env python3
#-*- coding : utf-8 -*-

__author__='Neverever'
'''
async web appliction
'''
import time
import json
import os
import asyncio
from aiohttp import web
import logging
logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Awesom</h1>')



async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at 9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
