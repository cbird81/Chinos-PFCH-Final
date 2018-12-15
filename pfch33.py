import requests as req
import json
import datetime as dt
import csv
from matplotlib import pyplot as plt


symbols = ('AAPL', 'MSFT', 'CSCO', 'CRM', 'BBY')
tsKey = 'Time Series (Daily)'
dataReqs = []
full = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+ \
                            "{}" + "&interval=5min&outputsize=full&apikey=6ID8FR3SLQFB2HWK"
small = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="+ \
                            "{}" + "&interval=5min&apikey=6ID8FR3SLQFB2HWK"

for s in symbols:
    dataReqs.append(req.get(small.format(s)))
    
firmsMomentsAdjClose = []
for index in range(len(dataReqs)):
	
	json = dataReqs[index].json()
	print(json.keys())
	json = json['Time Series (Daily)']
	xs, ys = [], []
	for key in json.keys():
	
		adjClose = json[key]["5. adjusted close"]
	
		
		moment = [symbols[index], dt.datetime.strptime(key, "%Y-%m-%d"), adjClose]
		firmsMomentsAdjClose.append(moment)
		
with open("final_adj_close.csv", 'w') as file:
	writer = csv.writer(file, delimiter=",")
	writer.writerows(firmsMomentsAdjClose)

for r in dataReqs:
	r.close()

