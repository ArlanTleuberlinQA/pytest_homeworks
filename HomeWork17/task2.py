import requests
import json

url = "https://swapi.dev/api/starships/10/"

response = requests.get(url)

data = response.json()


def get_homeworld_info(url):
    requests.get(url)
    return {'name': response.json()['name']}


pilots_info = []
for pilot_url in data['pilots']:
    pilot_data = requests.get(pilot_url).json()
    homeworld_info = get_homeworld_info(pilot_data['homeworld'])
    pilot_info = {
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld': homeworld_info,
        'homeworld_link': pilot_data['homeworld']
    }
    pilots_info.append(pilot_info)

millennium_falcon_data = {
    'name': data['name'],
    'max_speed': data['max_atmosphering_speed'],
    'class': data['starship_class'],
    'pilots': pilots_info
}

with open('millennium_falcon.json', 'w') as json_file:
    json.dump(millennium_falcon_data, json_file, indent=4)
