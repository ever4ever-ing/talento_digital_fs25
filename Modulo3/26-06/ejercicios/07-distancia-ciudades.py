from geopy.distance import geodesic

madrid = (40.4168, -3.7038)

valparaiso = (-33.047057, -71.620310)
distancia = geodesic(madrid, valparaiso).kilometers
print(f"La distancia entre Madrid y Valparaiso es de {distancia:.2f} km")