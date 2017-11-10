import requests
import json
import csv
class WeatherSpider(object):
    #csv doc header
    with open('jilin_weather.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(['date', 'week', 'Max temperature', 'Min temperature', 'rain rate'])
    def __inti__(self):
        pass
    def request(self,url):
        headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer': 'http://www.weather.com.cn/weather40d/101060201.shtml'
        }
        return requests.get(url,headers=headers)
    def create_url(self):
        year = '2016'
        for i in range(1,13):
            month = str(i) if i > 9 else "0" + str(i) 
            url = "http://d1.weather.com.cn/calendar_new/" + year + "/101060201_" + year + month + ".html"
            self.get_data(url)
    def get_data(self,url):
        respone = self.request(url).content
        json_str = respone.decode(encoding='utf-8')[11:]
        weathers = json.loads(json_str)
        for weather in weathers:
           
            data = [weather.get('date'),weather.get('wk'),weather.get('hmax'),weather.get('hmin'),weather.get('hgl')]
            with open('jilin_weather.csv', 'a') as f:   
                f_csv = csv.writer(f)
                f_csv.writerow(data)
if __name__ == '__main__':
    jl_weather = WeatherSpider()

