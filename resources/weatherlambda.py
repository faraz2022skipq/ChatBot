import urllib3

http = urllib3.PoolManager()
apitoken = "c22c535558cead35f179fe7e668cf71e"

city = input()
apiurl = "https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={APIkey}"
cityurl = apiurl.format(cityname=city, APIkey=apitoken)
r = http.request('GET', cityurl)
print(r)