from config import TOKEN
import requests
city = ("here")
url = f"https://api.waqi.info/feed/{city}/?token={TOKEN}"
response = requests.get(url)
data = response.json()
if data["status"] !="ok":
    print("Ooopsss, sorry, there was an error fetching AQI data.Try again later.")
    exit()
aqi = data["data"]["aqi"]
print(f"The AQI for {city}: {aqi}")
if aqi <= 50:
    print("Air quality is good, good time to work outdoors.Have a nice shift.")
elif aqi <= 100:
    print("Air quality is moderate, you can work outdoors.But be cautious.")
elif aqi <= 150:
    print("Air quality is unhealthy for sensitive groups,so check on your health.")
elif aqi <= 200:
    print("Air quality is unhealthy,wear a mask and have a break indoors.")
else:
    print("Air quality is super unhealthy,better stay at home.You deserve a break.")
    