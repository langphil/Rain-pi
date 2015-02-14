# Is it going to rain near me?
**Rain notifier for the Raspberry PI**

This simple python script runs on a Raspberry Pi. It runs at set intervals, checking a weather API. You can set longitude & latitude coordinates to recieve notifications to see if weather is due near a set location over the next period. 

This is achieved by employing the Wunderground API, a python script and a Raspberry Pi with a PiBord LED setup, or similar hardware. 

1) Get yourself an RPI with Raspbian and a PiBorg LED setup.

2) Install PiBorg by following the instructions at [Piborg](www.piborg.org/ledborg). 

3) Go to [Wundeground](http://api.wunderground.com/weather/api/) & get yourself an API key.

4) Work out the [coordinates](http://www.findlatitudeandlongitude.com/) that you'd like to get notifications for.

5) Enter all three values (API, Lon, Lat) into the URL in line 9 of forecast.py

6) Set pop value (% chance of rain **0 - 100**) on line 21 of forecast.py

7) Setup up a [cron job](http://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/) to run the script at intervals.

8) Your light should now turn on everytime the script runs and the percentage chance of rain occuring in your location is higher than the pop value you have set. 

9) Find a pretty glass structure to place your pi within and put it on a shelf / rain jacket closet.

10) Wait for rain....
