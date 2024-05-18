from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from RedisReq.RedReq import redis_get
from datetime import datetime


NIGHT = [0, 1, 2, 3, 20, 21, 22, 23]


async def ge(pointA, pointB):
    
    if datetime.now().hour in NIGHT:
        tar = int(redis_get('tarif_night'))
        TUMB = "НОЧЬ"
        
    else:
        TUMB = "ДЕНЬ"
        tar = int(redis_get('tarif_day'))
    
    tpA = (pointA.latitude, pointA.longitude)
    tpB = (pointB.latitude, pointB.longitude)
    
    distance = geodesic(
        tpA,
        tpB
        ).kilometers

    A, B = await get_gps(tpA, tpB)
    
    return f"""Маршрут от: |{A}|

до

|{B}|

Расстояние: |{round(distance, 2)} км|

Итоговая цена = {round(distance, 2) * tar :.2f} руб по тарифу {TUMB}"""



async def get_gps(pointA, pointB):
    loc = Nominatim(user_agent='user')
    
    locationA = loc.reverse(pointA)
    locationB = loc.reverse(pointB)
    
    return locationA, locationB