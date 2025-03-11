import requests

url = 'https://detest-bsd7.onrender.com/predict'

data = {

    'highest_value': 70000000,
    'appearance': 104		,
    'minutes_played':9390,
    'award': 13		,
}

response = requests.post(url, json=data)

print(response.json())