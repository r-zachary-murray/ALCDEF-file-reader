import numpy as np
import os
from os import listdir
from os.path import isfile, join

def readfile(myfile):

	with open(myfile) as f:
		lines = f.readlines()
	    
	lines = [line.rstrip('\r\n') for line in lines]

	startlines =[]
	endlines = []

	for i in range(len(lines)):
		if lines[i] == 'STARTMETADATA':
			startlines.append(i)
		if lines[i] == 'ENDMETADATA':
			endlines.append(i)
		
	startlines.append(len(lines))

	allheaders = []
	alldata = []

	for j in range(len(startlines)-1):

		header = {}
		data = {}

		for i in range(startlines[j]+1, endlines[j]):
			dat = lines[i].split('=')
			header[dat[0]]=dat[1]

		tmpray = []
		for i in range(endlines[j]+1, startlines[j+1]):
			dat = lines[i].split('=')[1]
			rows = dat.split('|')
			tmpray.append(rows)

		tmpray = np.asarray(tmpray).T
		data["TIME"]  = tmpray[0].astype(float)
		data["MAG"]  = tmpray[1].astype(float)
		data["ERR"] = tmpray[2].astype(float)
	
		allheaders.append(header)
		alldata.append(data)

	return allheaders, alldata
