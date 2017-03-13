#!/usr/bin/env python3
from sys import argv

ctr=0
for x in range(1930, 2001):
	print "wget --output-document="+str(x)+"11.xml http://earthquake.usgs.gov/fdsnws/event/1/query?format=xml\&starttime="+str(x)+"-"+str(ctr)+"-01\&endtime="+str(x)+"-11-01"

