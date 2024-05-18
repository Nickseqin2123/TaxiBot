import asyncio
import aiomysql


async def connect():
    return await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='NekitVip123_ZXCPUDGE228',
                                      db='mysql', loop=asyncio.get_running_loop())