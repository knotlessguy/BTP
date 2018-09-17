import googlemaps
import gspread
import time

from oauth2client.service_account import ServiceAccountCredentials

scope= ['https://spreadsheets.google.com/feeds']
creds= ServiceAccountCredentials.from_json_keyfile_name('secret.json',scope)
client=gspread.authorize(creds)

sheet=client.open('Thane_travel_data').sheet1

eef_lat = [18.952563,18.909179,18.956634,18.981705,19.017676,19.142981,19.21418,19.267896]
eef_long = [72.960334,72.986411,73.036789,73.088119,73.106271,73.046689,73.012196,73.080997]

timestamp = time.strftime('%H:%M')
present_time=time.time()
gmaps = googlemaps.Client(key='AIzaSyBVd5uRVv5gGyvs8Zh9nDWVV96rCVU7LvI')
i = int(sheet.cell(189, 2).value)

for x in range (0,7):
    origins=(eef_lat[x],eef_long[x])
    destinations=(eef_lat[x+1],eef_long[x+1])
    my_distance = gmaps.distance_matrix(origins,destinations,departure_time=present_time)
    live_data = my_distance['rows'][0]['elements'][0]['duration_in_traffic']['text']
    sheet.update_cell(i+2,x+2, live_data)

sheet.update_cell(i+2,1,timestamp)

i=i+1
new=str(i)
sheet.update_cell(189,2,new)
