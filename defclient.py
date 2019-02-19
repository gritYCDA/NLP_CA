def SnRdata(filepointer):
	# -*- coding: utf-8 -*-
	import requests 
	import csv
	import json

	# api-endpoint 
	URL = "http://192.168.86.242:8080"
	
	#filepointer is csv file
	rdr = csv.reader(filepointer)
	datadic = {}
	count = 0
	for line in rdr:
		datadic[str(count)] = str(line)[:128]
		count += 1

	for x in datadic.keys():
		print(x)
		print(datadic[x])
	
	#send and receive data
	r = requests.post(url = URL, json=PARAMS) 

	#data parsing to json
	data = r.json() 
	
	print("=============json=============")
	print(data)
	print("=============json=============")
	print()
	
	for i in range(len(data)):
		print("DATA_"+str(i))
		print('|| negative_per : ' + str("{0:.4f}".format(data[str(i)]['negative_per'])) )
		print('|| neutral_per : ' + str("{0:.4f}".format(data[str(i)]['neutral_per'])) )
		print('|| positive_per : ' + str("{0:.4f}".format(data[str(i)]['positive_per'])) )
		print()