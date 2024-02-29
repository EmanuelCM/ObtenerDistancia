import folium
import pandas as pd
from geopy.distance import geodesic 


latitud1="-8.1078082"
longitud1="-79.01667613"

latitud2="-8.110245338581"
longitud2="-79.01737465745"

punto1= (latitud1,longitud1)
punto2= (latitud2,longitud2)

distancia=geodesic((latitud1,longitud1),(latitud2,longitud2)).m
if distancia<300.00:
    print(distancia)
else:
    print ("fuera de rango")


