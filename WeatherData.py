"""
Created on Tue Oct 10 19:18 2017

@author: Palchandar
"""
import requests
import csv
from dateutil.rrule import *
from dateutil.parser import *
from datetime import datetime

# Variables
api = '3909bb9bd13eaf33' # Palchandar(developer) API key

# Number of weather stations in numeric-from 1 to many
n= input('Enter number of weather stations you want to check: ')
stations = []
for i in xrange(1, n+1):
      stations.append(raw_input('Enter weather station %s ID: '% (i)))  # weather station ID :- ex: "YSSY" for SYDNEY

daySt = raw_input('Enter Start date in yyyymmdd format : ')
dayEnd = raw_input('Enter End date in yyyymmdd format : ')

#output path - /Users/Palchandar/Output/
outPath = raw_input('Enter output location to store extracted data ex- "/Path/Path/" : ')

# Create list of dates between start and end
days = list(rrule(DAILY, dtstart=parse(daySt), until=parse(dayEnd)))


with open(outPath + daySt + '-' + dayEnd + '.csv', 'wb') as csvfile:
	f = csv.writer(csvfile)
	f.writerow(["station","location","datetime", "tempm", "tempi", "dewptm", "dewpti", "hum", "wspdm", "wspdi", "wgustm", "wgusti", "wdird", "wdire", "vism", "visi", "pressurem", "pressurei", "windchillm", "windchilli", "heatindexm", "heatindexi", "precipm", "precipi", "conds", "fog", "rain", "snow", "hail", "thunder", "tornado"])

	for station in stations:
	    for day in days:
		    r = requests.get('http://api.wunderground.com/api/' + api + '/history_' + day.strftime("%Y%m%d") + '/q/' + station + '.json')
		    data = r.json()['history']['observations']
		    for elem in data:
			    f.writerow([(elem["date"]["tzname"].split("/")[1][0:3]).upper(),elem["date"]["tzname"].split("/")[0],elem["utcdate"]["year"] + elem["utcdate"]["mon"] + elem["utcdate"]["mday"] + 'T' + elem["utcdate"]["hour"] + elem["utcdate"]["min"], elem["tempm"], elem["tempi"], elem["dewptm"], elem["dewpti"], elem["hum"], elem["wspdm"], elem["wspdi"], elem["wgustm"], elem["wgusti"], elem["wdird"], elem["wdire"], elem["vism"], elem["visi"], elem["pressurem"], elem["pressurei"], elem["windchillm"], elem["windchilli"], elem["heatindexm"], elem["heatindexi"], elem["precipm"], elem["precipi"], elem["conds"], elem["fog"], elem["rain"], elem["snow"], elem["hail"], elem["thunder"], elem["tornado"]])
   
	print "\nCOMPLETED!!! Please check output location for extracted data"