import yaml
import json
import os

from pypinyin import lazy_pinyin

hospitals = {}

for filename in os.listdir('data'):
    if filename.endswith('.yml') and (not filename.startswith('example')):
        file = 'data/' + filename
        print('Loading - ' + file)
        with open(file, 'r', encoding='utf-8') as stream:
            hospital = yaml.load(stream)
            city = hospital['city']
            name = hospital['name']
            if city not in hospitals:
                hospitals[city] = {}
            hospitals[city][name] = hospital

try:
    os.mkdir('output')
except FileExistsError:
    pass

cities = {}
for city in hospitals:
    city_filename = "".join(lazy_pinyin(city)) + '.json'
    cities[city] = city_filename
    json.dump(hospitals, open('output/'+ city_filename, 'w'), ensure_ascii=False, indent=2)

json.dump(cities, open('output/hospitals.json', 'w'), ensure_ascii=False, indent=2)
