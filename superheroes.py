import requests
from pprint import pprint
import json


def get_the_smartest_superhero() -> str:
    the_smartest_superhero = ''
    intelligence = 0
    base_url = "https://akabab.github.io/superhero-api/api"
    url = base_url + "/all.json"
    response = requests.get(url)
    heroes_list = response.json()
    heroes_names = ['Hulk', 'Captain America', 'Thanos']
    filtered_heroes_list = [hero for hero in heroes_list if hero['name'] in heroes_names]
    for hero in filtered_heroes_list:
        if hero['powerstats']['intelligence'] > intelligence:
            intelligence = hero['powerstats']['intelligence']
            the_smartest_superhero = hero['name']
    return the_smartest_superhero

print(get_the_smartest_superhero())