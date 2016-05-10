import yaml
import json
import os

hospitals = {}

for filename in os.listdir('data'):
    if filename.endswith('.yml') and (not filename.startswith('example')):
        file = 'data/' + filename
        print('Loading - ' + file)
        with open(file, 'r') as stream:
            hospital = yaml.load(stream)
            city = hospital['city']
            name = hospital['name']
            if city not in hospitals:
                hospitals[city] = {}
            hospitals[city][name] = hospital

json.dump(hospitals, open('output/hospitals.json', 'w'), ensure_ascii=False, indent=2)
