import requests
from pprint import pprint


def get_the_smartest_superhero_from_list() -> str:
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

def get_the_smartest_superhero(superheros: list):
   the_smartest_superhero = ''
   max_intelligence = 0
   base_url = "https://akabab.github.io/superhero-api/api"
   for hero_id in superheros:
       url = base_url + f'/id/{hero_id}.json'
       response = requests.get(url)
       hero_info = response.json()
       if hero_info['powerstats']['intelligence'] > max_intelligence:
           max_intelligence = hero_info['powerstats']['intelligence']
           the_smartest_superhero = hero_info['name']
   return the_smartest_superhero
