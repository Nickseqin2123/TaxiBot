from geopy.geocoders import Nominatim
from geopy.distance import geodesic


async def ge(pointA, pointB):
    
    tpA = (pointA.latitude, pointA.longitude)
    tpB = (pointB.latitude, pointB.longitude)
    
    distance = geodesic(
        tpA,
        tpB
        ).kilometers

    A, B = await get_gps(tpA, tpB)
    
    return f"""Маршрут от {A}

до

{B}

Итоговая цена = {round(distance, 2) * 10 :.2f} руб. за {round(distance, 2)} км"""


async def get_gps(pointA, pointB):
    loc = Nominatim(user_agent='user')
    
    locationA = loc.reverse(pointA)
    locationB = loc.reverse(pointB)
    
    return locationA, locationB