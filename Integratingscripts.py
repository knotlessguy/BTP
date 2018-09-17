import requests
import googlemaps
from datetime import datetime

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'
params1 = {
            'address': 'Powai, IIT Bombay',
            'sensor': 'false',
            'region': 'india'
        }
params2 = {
            'address': 'Ghansoli Naka, Navi Mumbai',
            'sensor': 'false',
            'region': 'india'
        }

        # Do the request and get the response data
req1 = requests.get(GOOGLE_MAPS_API_URL, params=params1)
res1 = req1.json()

req2 = requests.get(GOOGLE_MAPS_API_URL, params=params2)
res2 = req2.json()

        # Use the first result
result1 = res1['results'][0]

geodata = dict()
geodata['lat'] = result1['geometry']['location']['lat']
geodata['lng'] = result1['geometry']['location']['lng']
geodata['address'] = result1['formatted_address']

print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
print(geodata['lat'])
print(geodata['lng'])
print(geodata['address'])

result2 = res2['results'][0]

geodata1 = dict()
geodata1['lat'] = result2['geometry']['location']['lat']
geodata1['lng'] = result2['geometry']['location']['lng']
geodata1['address'] = result2['formatted_address']

print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata1))
print(geodata1['lat'])
print(geodata1['lng'])
print(geodata1['address'])


# Below is the second part of the program to be implemented
# gmaps = googlemaps.Client(key='AIzaSyBVd5uRVv5gGyvs8Zh9nDWVV96rCVU7LvI')
#
#
# now = datetime.now()
# directions_result = gmaps.directions("18.997739, 72.841280",
#                                      "18.880253, 72.945137",
#                                      mode="driving",
#                                      avoid="ferries",
#                                      departure_time=now
#                                     )
#
# print(directions_result[0]['legs'][0]['distance']['text'])
# print(directions_result[0]['legs'][0]['duration']['text'])
