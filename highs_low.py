import csv
import matplotlib.pyplot as plt
from datetime import datetime

#filename = 'sitka_weather_07-2014.csv' 
filename1 = 'sitka_weather_2014.csv'
filename2 = 'death_valley_2014.csv'



def get_weather_data(filename):
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)
		#print(header_row)
		#for index, column_header in enumerate(header_row):
			#print(index, column_header)
	
		for row in reader:
			try:
				high = int(row[1])
				low = int(row[3])
				current_date = datetime.strptime(row[0], "%Y-%m-%d")
			except ValueError:
				print(current_date, "Missing data")
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)

dates, highs, lows = [], [], []

get_weather_data(filename1)
#print(dates)


fig = plt.figure(dpi=64, figsize=(10,6))
#plt.plot(dates, highs, c='red')
#plt.plot(dates, lows, c='blue')

get_weather_data(filename2)
print(highs)
plt.plot(dates, highs, c='yellow')
plt.plot(dates, lows, c='gray')

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("Daily high/low temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()	

