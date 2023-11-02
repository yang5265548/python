#Write a program that fetches and prints out a random Chuck Norris joke for the user.
# Use the API presented here: https://api.chucknorris.io/. The user should only be shown the joke text.

import requests

request = "https://api.chucknorris.io/jokes/random"
# {'categories': [], 'created_at': '2020-01-05 13:42:26.766831', 'icon_url': 'https://assets.chucknorris.host/img/avatar/chuck-norris.png', 'id': 'q2TDffchRcSjC8ZBcNO8PQ', 'updated_at': '2020-01-05 13:42:26.766831', 'url': 'https://api.chucknorris.io/jokes/q2TDffchRcSjC8ZBcNO8PQ', 'value': 'You will get a bloody nose even if Chuck Norris only thinks about punching you in the face.'}
nums=int(input("please enter the nums of the jokes: "))
for i in range(nums):
    response = requests.get(request).json()
    joke = response["value"]
    print(joke)
