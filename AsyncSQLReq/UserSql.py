from AsyncSQLReq.connect import connect
from aiomysql import Pool, DictCursor, Cursor


class UserRequests:
    async def add_pool(self):
        self.pool: Pool = await connect()
    
    async def get_user_phone(self, user_id):
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(Cursor) as cursa:
                    await cursa.execute(
                        f'SELECT id FROM taxi.telephone_numbers WHERE id = {user_id}'
                    )
                    return await cursa.fetchall()
        except Exception as er:
            print(er)
    
    async def get_tar(self):
        print('OK')
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(DictCursor) as cursa:
                    await cursa.execute(
                        'SELECT * FROM taxi.tarifs'
                    )
                    return await cursa.fetchall()
        except Exception as er:
            print(er)
    
    async def set_user_phone(self, user_id, tel_num):
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(DictCursor) as cursa:
                    req = f"""INSERT INTO `taxi`.`telephone_numbers` (`id`, `tn`)
                    VALUES ('{user_id}', '{tel_num}')"""
                    await cursa.execute(
                        req
                    )
                    await conn.commit()
        except Exception as er:
            print(er)
            
    async def regist_order(self, user_id, text):
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(DictCursor) as cursa:
                    req = f"""INSERT INTO `taxi`.`orders`
                    (`user_id`, `information`)
                    VALUES ('{user_id}', '{text}')"""
                    
                    await cursa.execute(
                        req
                    )
                    await conn.commit()
        except Exception as er:
            print(er)
    
    async def get_orders(self, user_id):
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(DictCursor) as cursa:                    
                    await cursa.execute(
                        f'SELECT * FROM taxi.orders WHERE user_id = "{user_id}"'
                    )
                    return await cursa.fetchall()
        except Exception as er:
            print(er)

    async def del_orders(self, user_id):
        try:
            async with self.pool.acquire() as conn:
                async with conn.cursor(DictCursor) as cursa:                    
                    await cursa.execute(
                        f'DELETE FROM `taxi`.`orders` WHERE `user_id` = "{user_id}"'
                    )
                    await conn.commit()
        except Exception as er:
            print(er)


database = UserRequests()