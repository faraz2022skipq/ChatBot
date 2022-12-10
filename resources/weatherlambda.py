import urllib3
import json
from types import SimpleNamespace

http = urllib3.PoolManager()
apitoken = "c22c535558cead35f179fe7e668cf71e"

def lambda_handler(event, context):
    
    city = event["inputTranscript"]
    print(city)
    
    apiurl = "https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={APIkey}&units=metric"
    cityurl = apiurl.format(cityname=city, APIkey=apitoken)
    requestresponse = http.request('GET', cityurl)
    data = requestresponse.data
    x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    temp = x.main.temp
    print("TEMPERATURE ", temp)
    return temp
    
