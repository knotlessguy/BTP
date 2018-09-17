import simplejson, urllib
orig_coord = orig_lat, orig_lng
dest_coord = dest_lat, dest_lng
url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord),str(dest_coord))
result= simplejson.load(urllib.urlopen(url))
driving_time = result['rows'][0]['elements'][0]['duration']['value']