from gpiozero import LED
from time import sleep
from urllib2 import urlopen
import json
from signal import pause

led = LED(17)
led1 = LED(18)
led2 = LED(23)
led3 = LED(24)
req = urlopenreq = urlopen('http://api.wunderground.com/api/ce79588428cec41f/fo$
parsed_json = json.load(req)
pop = int(parsed_json['forecast']['txt_forecast']['forecastday'][0]['pop'])

print 'Current chance of precipitation is {}.'.format(pop)

if pop > 70:
    led.on()
    led1.on()
    led2.on()
    led3.on()
    pause()
    print "Here comes the rain"

else:
    led.off()
    led1.off()
    led2.off()
    led3.off()
    print "No rain!"
