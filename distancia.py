from math import cos,radians,sin,pow,asin,sqrt

#A partir de la latitud y longitud de dos lugares, se calcula la distancia entre ellos
#https://es.wikipedia.org/wiki/F%C3%B3rmula_del_haversine

def distancia(lat1, long1, lat2, long2):
    radio = 6371 #de la tierra

    lat1 = radians(lat1)
    lat2 = radians(lat2)
    long1 = radians(long1)
    long2 = radians(long2)

    dlat = lat2-lat1
    dlon = long2-long1

    a = pow(sin(dlat/2),2) + cos(lat1)*cos(lat2)*pow(sin(dlon/2),2)
    dist = 2 * radius * asin(sqrt(a))
    return dist
