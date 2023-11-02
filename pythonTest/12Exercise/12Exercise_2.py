#Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api.
# Your task is to write a program that asks the user for the name of a municipality
# and then prints out the corresponding weather condition description text and temperature in Celsius degrees.
# Take a good look at the API documentation.
# You must register for the service to receive the API key required for making API requests.
# Furthermore, find out how you can convert Kelvin degrees into Celsius.

import requests


# {'categories': [], 'created_at': '2020-01-05 13:42:26.766831', 'icon_url': 'https://assets.chucknorris.host/img/avatar/chuck-norris.png', 'id': 'q2TDffchRcSjC8ZBcNO8PQ', 'updated_at': '2020-01-05 13:42:26.766831', 'url': 'https://api.chucknorris.io/jokes/q2TDffchRcSjC8ZBcNO8PQ', 'value': 'You will get a bloody nose even if Chuck Norris only thinks about punching you in the face.'}

# for i in range(nums):
#     response = requests.get(request).json()
#     joke = response["value"]
#     print(joke)

key="ab6f7f025431e93f04eaafccdb34df98"
cityname=input("please enter name of the municipality: ")
# limit=input("please enter the num of the limit: ")
ladrequest=f"http://api.openweathermap.org/geo/1.0/direct?q={cityname}&limit=5&appid={key}"
response = requests.get(ladrequest).json()
lat=response[0]["lat"]
lon=response[0]["lon"]
unit=input("please enter the unit of the temperature: imperial/metric/standard~~~")
# part=input("please enter the parts:current/minutely/hourly/daily/alerts___")
# weatherResponse=f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}"
weatherResponse=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units={unit}"
response = requests.get(weatherResponse).json()
description=response["weather"][0]["description"]
temp=response["main"]["temp"]
print(response)
print(f"{cityname} 's wheather is {description},the temp is {temp} ")

