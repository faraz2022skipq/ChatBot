import urllib3
import json

http = urllib3.PoolManager()
apitoken = "c22c535558cead35f179fe7e668cf71e"

city = "Lahore"
apiurl = "https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={APIkey}&units=metric"
cityurl = apiurl.format(cityname=city, APIkey=apitoken)
requestresponse = http.request('GET', cityurl)
data = requestresponse.data
print(data['b'])