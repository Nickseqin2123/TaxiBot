import pymysql
import pymysql.cursors


class Database:

    HOST = '127.0.0.1'
    USER = 'root'
    DATABASE = 'taxi'
    PASSWORD = 'NekitVip123_ZXCPUDGE228'

    @staticmethod
    def get_tar() -> dict:
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
                    cursa.execute('SELECT * FROM taxi.tarifs')

                    return cursa.fetchall()
            finally:
                connect.close()

        except Exception as er:
            print(er)

    @staticmethod
    def set_tar(price_day, price_night) -> None:
        try:
            connect = pymysql.connect(
                host=Database.HOST,
                password=Database.PASSWORD,
                database=Database.DATABASE,
                user=Database.USER,
                port=3306,
                cursorclass=pymysql.cursors.DictCursor
            )
            print('OK')
            try:
                with connect.cursor() as cursa:
                    req = f'''UPDATE `taxi`.`tarifs`
                    SET tarif_day = "{price_day}",
                    tarif_night = "{price_night}"'''
                    cursa.execute(req)
                    connect.commit()

            finally:
                connect.close()

        except Exception as er:
            print(er)
    
    @staticmethod
    def set_user_phone(user_id: int, phone_number: str) -> None:
        try:
            connect = pymysql.connect(
                host=Database.HOST,
                password=Database.PASSWORD,
                database=Database.DATABASE,
                user=Database.USER,
                port=3306,
                cursorclass=pymysql.cursors.DictCursor
            )
            print('OK')
            try:
                with connect.cursor() as cursa:
                    req = f"""INSERT INTO `taxi`.`telephone_numbers` (`id`, `tn`)
                    VALUES ('{user_id}', '{phone_number}')"""
                    cursa.execute(req)
                    connect.commit()

            finally:
                connect.close()

        except Exception as er:
            print(er)
    
    @staticmethod
    def get_user_phone(user_id: int) -> None:
        try:
            connect = pymysql.connect(
                host=Database.HOST,
                password=Database.PASSWORD,
                database=Database.DATABASE,
                user=Database.USER,
                port=3306,
                cursorclass=pymysql.cursors.Cursor
            )
            print('OK')
            try:
                with connect.cursor() as cursa:
                    cursa.execute(f'SELECT * FROM taxi.telephone_numbers WHERE id = {user_id}')
                    return cursa.fetchall()
                    
            finally:
                connect.close()

        except Exception as er:
            print(er)