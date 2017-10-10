The Weather
===========

Python script for parsing multiple days of historical weather data from Weather Underground

**NOTE:** _This script rely on the [Weather Underground](http://www.wunderground.com/) [API](http://www.wunderground.com/weather/api/).  You will need to obtain your own free API key [here](http://www.wunderground.com/weather/api/d/pricing.html)._

| Script | Description | Requirements |
| ------ | ----------- | ------------ |
| WeatherData.py | Grabs JSON from URL and saves to a CSV file | Request module |

[Requests module](http://docs.python-requests.org/en/latest/) installation instructions found [here](http://docs.python-requests.org/en/latest/user/install/).

IDE Choice:

Spyder [here](https://pythonhosted.org/spyder/installation.html).

Jupyter Notebook for interactive explore: Available from Anaconda Python distrubution [here](https://www.continuum.io/downloads).

Variables to change:

| Variable | Description |
| -------- | ----------- |
| daySt | Start date in YYYYMMDD format |
| dayEnd | End date  in YYYYMMDD format |
| outPath | path to output directory to save files |
| stations | station ID (search [here](http://www.wunderground.com/history/)) |
| api | developer API Key obtained [here](http://www.wunderground.com/weather/api/d/pricing.html) |

Output Field descriptions [here](http://www.wunderground.com/weather/api/d/docs?d=resources/phrase-glossary).

Usage:
$ Python WeatherData.py

Stations for example ( Check the stations link for more location):
YMML:Melbourne, Australia; NZCH:Christchurch, New Zealand; WIIK:Kalijati, Indonesia; VOBG:Bangalore, India; ZSSS:Shanghai Hongqiao, China; RJTI:Tokyo, Japan; UUWW:Moscow Vnukovo, Russia; EGMC:London, United Kingdom; FADN:Durban, South Africa; KSFO:San Francisco, CA; CXTO :Toronto City, Ontario; SLCO:Cobija, Bolivia; OMDB : Dubai, UAE
