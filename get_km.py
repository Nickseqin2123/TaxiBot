from geopy.geocoders import Nominatim
from geopy.distance import geodesic


loc = Nominatim(user_agent='GetLoc')
a = 'Чувашская Республика, Пархикасы, ул.Шоссейная 17'
b = 'Чувашская Республика, Чебоксары, ул.Патриса Лумумбы'

getLocA = loc.geocode(a)

getLocB = loc.geocode(b)

distance = geodesic((getLocA.latitude, getLocA.longitude), (getLocB.latitude, getLocB.longitude)).kilometers

print(f"""Маршрут от {a} до {b}
Итоговая цена = {round(distance, 2) * 10 :.2f} руб. за {round(distance, 2)} км""")