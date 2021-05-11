import requests

s_city = "Odessa, UA"
city_id = 0
appid = "7419d271517c63603aad9ee3c3fc9504"

try:
    res = requests.get("https://api.openweathermap.org/data/2.5/find",
        params={'q' : s_city, 'type' : 'like', 'units' : 'metric', 'lang' : 'RU', 'APPID' : appid})
    data = res.json()
    print("conditions:", data['weather'][0]['description'])
    print("temp:", data['main']['temp'])
    print("temp_min:", data['main']['temp_min'])
    print("temp_max:", data['main']['temp_max'])
except Exception as e:
    print("Exception (find)", e)
    pass