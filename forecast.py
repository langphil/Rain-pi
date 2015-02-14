from urllib2 import urlopen
import json

# Simply get your API key from Wunderground.com
# Enter your API KEY into the .json line
# Query Wunderground for the required longitude and latitude
# Enter the values into the URL below

req = urlopenreq = urlopen('http://api.wunderground.com/api/API_KEY/forecast/q/LONGITUDE,LATITUDE.json')
	parsed_json = json.load(req)
pop = int(parsed_json['forecast']['txt_forecast']['forecastday'][0]['pop'])

# pop = 0

print 'Current chance of precipitation is {}.'.format(pop)

# The default setting is to turn on the LED
# for any chance of rain above 20%. You can adjust
# the value in "if pop > 20:"

if pop > 70:
        execfile ("/home/pi/rain.py")
        print ('Rain!')

else:
        execfile ("/home/pi/rain_no.py")
        print ('No rain!')
