#!/usr/bin/env python3
from sys import argv

ctr=0
for x in range(1930, 2017):
	for y in range(1, 12):
		ctr=ctr+1
		print "wget --output-document="+str(x)+str(ctr)+".csv http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv\&starttime="+str(x)+"-"+str(ctr)+"-01\&endtime="+str(x)+"-"+str(ctr+1)+"-01"
		if ctr==11:
			print "wget --output-document="+str(x)+str(ctr+1)+".csv http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv\&starttime="+str(x)+"-"+str(ctr+1)+"-01\&endtime="+str(x+1)+"-"+str(ctr-10)+"-01"
	ctr=0

