import requests
import os

my_secret = os.environ['BING_MAPS_KEY']


PRECIO_BASE = 4000

BING_KEY = my_secret


def geocode(dir1):
  
  address = dir1.replace("#", " ")
  response= requests.get(f'http://dev.virtualearth.net/REST/v1/Locations?adminDistrict=CO-ATL&locality=Barranquilla&addressLine={address}&key={BING_KEY}&countryRegion=CO')
  res = response.json()
  
  coordinates = res['resourceSets'][0]['resources'][0]['point']['coordinates']
  lat = coordinates[0]
  lon = coordinates[1]
  coor = f"{lat},{lon}"
  print(coor)
  return coor

def distancia(coordenadas1, coordenadas2):
  res = requests.get(f"https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins={coordenadas1}&destinations={coordenadas2}&travelMode=driving&key={BING_KEY}").json()
  print(res)
  distancia = res["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
  print( f"Una distancia de {distancia}m")
  return distancia

def guardar(direccion1,nombre1, direccion2, nombre2, precio, distancia):
  

  
  
