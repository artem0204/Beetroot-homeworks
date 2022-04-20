import requests
import time
import pprint
import json


def get_the_weather():
    city_name = input("Enter your city: ")
    params = {"units": "metric"}
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=515fb3364f45247a947299b3e18b24fa"
    req = requests.get(base_url, params=params)
    resp = req.json()
    try:
        condition = resp['weather'][0]['main']
    except KeyError:
        result = f"ERROR. Such {city_name} is not exists "

    tempr = float(resp['main']['temp'])
    tempr_min = float(resp['main']['temp_min'])
    tempr_max = float(resp['main']['temp_max'])
    pressure = resp['main']['pressure']
    humidity = resp['main']['humidity']
    sunrise = time.strftime("%H:%M:%S",time.gmtime(resp['sys']['sunrise']))
    sunset = time.strftime("%H:%M:%S", time.gmtime(resp['sys']['sunset']))

    final_info = condition+"\n"+str(tempr)+"C"
    final_data = "\n"+"max temp: "+str(tempr_max)+ "\n"+"min temp: "+str(tempr_min)+\
        "\n"+"pressure: "+str(pressure)+\
        "\n"+"humidity: "+str(humidity)+\
        "\n"+"sunrise: "+str(sunrise)+\
        "\n"+"sunset: " + str(sunset)
    print(final_info)
    print(final_data)

if __name__=="__main__":
    get_the_weather()