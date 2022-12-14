import urllib3
import json
from types import SimpleNamespace

http = urllib3.PoolManager()
apitoken = "***"

def lambda_handler(event, context):
    
    city = event["interpretations"][0]["intent"]["slots"]["city"]["value"]["interpretedValue"]
    
    apiurl = "https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={APIkey}&units=metric"
    cityurl = apiurl.format(cityname=city, APIkey=apitoken)
    requestresponse = http.request('GET', cityurl)
    data = requestresponse.data
    weather = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
    temperature = weather.main.temp
    feelslike = weather.main.feels_like
    mintemp = weather.main.temp_min
    maxtemp = weather.main.temp_max
    humidity = weather.main.humidity
    windspeed = weather.wind.speed
    
    messagecontent = """Temperature = {tem}, 
            Feels like = {feel}, Speed = {speed} m/s,
            Humidity = {humidity}%""".format(tem = temperature, feel = feelslike, speed = windspeed, humidity = humidity)
    
    response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close",
                },
                "intent": {
                    "name": "WeatherBot",
                    "state": "Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": messagecontent
                }
            ]
        }
    return response