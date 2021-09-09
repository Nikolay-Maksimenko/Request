import requests

url_search_name = "https://superheroapi.com/api/2619421814940190/search/"
superheroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]

def get_most_int_hero(url, names):
    best_intelligence_value = 0
    for superhero in names:
        superhero_inf = requests.get(url + superhero['name'])
        superhero['intelligence'] = int(superhero_inf.json()['results'][0]['powerstats']['intelligence'])
        if superhero['intelligence'] > best_intelligence_value:
            best_intelligence_value = superhero['intelligence']
            most_intelligent_hero = superhero['name']
    print(most_intelligent_hero)

get_most_int_hero(url_search_name, superheroes)