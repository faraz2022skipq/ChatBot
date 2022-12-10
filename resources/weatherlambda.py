import urllib3
import json
from types import SimpleNamespace

def lambda_handler(event, context):
    print(event)

http = urllib3.PoolManager()
apitoken = "c22c535558cead35f179fe7e668cf71e"

city = "Lahore"
apiurl = "https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={APIkey}&units=metric"
cityurl = apiurl.format(cityname=city, APIkey=apitoken)
requestresponse = http.request('GET', cityurl)
data = requestresponse.data
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
temp = x.main.temp
# return temp