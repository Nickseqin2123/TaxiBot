import pymysql
import pymysql.cursors

from SqlReq.SqlRequests import Database


class NextReq(Database):
    
    @staticmethod
    def regist_order(user_id, text) -> None:
        try:
            connect = pymysql.connect(
                password=Database.PASSWORD,
                host=Database.HOST,
                port=3306,
                database=Database.DATABASE,
                user=Database.USER,
                cursorclass=pymysql.cursors.DictCursor
            )
            print('OK')
            try:
                with connect.cursor() as cursa:
                    req = f"""INSERT INTO `taxi`.`orders`
                    (`user_id`, `information`)
                    VALUES ('{user_id}', '{text}')"""
                    cursa.execute(req)
                    connect.commit()
            finally:
                connect.close()

        except Exception as er:
            print(er)
    
    @staticmethod
    def get_orders(user_id):
        try:
            connect = pymysql.connect(
                password=Database.PASSWORD,
                host=Database.HOST,
                port=3306,
                database=Database.DATABASE,
                user=Database.USER,
                cursorclass=pymysql.cursors.DictCursor
            )
            print('OK')
            try:
                with connect.cursor() as cursa:
                    cursa.execute(f'SELECT * FROM taxi.orders WHERE user_id = "{user_id}"')
                    return cursa.fetchall()
            finally:
                connect.close()

        except Exception as er:
            print(er)
    
    
    @staticmethod
    def del_orders(user_id):
        try:
            connect = pymysql.connect(
                password=Database.PASSWORD,
                host=Database.HOST,
                port=3306,
                database=Database.DATABASE,
                user=Database.USER,
                cursorclass=pymysql.cursors.DictCursor
            )
            print('OK')
            try:
                with connect.cursor() as cursa:
                    cursa.execute(f'DELETE FROM `taxi`.`orders` WHERE `user_id` = "{user_id}"')
                    connect.commit()
                    
            finally:
                connect.close()

        except Exception as er:
            print(er)


database = NextReq()
database.del_orders(1124518724)