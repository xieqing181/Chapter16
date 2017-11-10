import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv' 

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#print(header_row)
	#for index, column_header in enumerate(header_row):
		#print(index, column_header)
		
	dates, highs = [], []
	for row in reader:
		high = int(row[1])
		highs.append(high)
		current_date = datetime.strptime(row[0], "%Y-%m-%d")
		#current_date = row[0]
		dates.append(current_date)
	print(dates)
	print(current_date)
