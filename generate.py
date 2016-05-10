import os
import sys

import yaml
import json

from jinja2 import Template
from pypinyin import lazy_pinyin


def render_html(template_file, dist_file, **kwargs):
    with open(template_file, 'r') as f:
        template = Template(f.read())
        html = template.render(kwargs)
        with open(dist_file, 'w') as f:
            f.write(html)


def do_generate(version):
    hospitals = {}

    for filename in os.listdir('data'):
        if filename.endswith('.yml') and (not filename.startswith('example')):
            file = 'data/' + filename
            print('Loading - ' + file)
            with open(file, 'r', encoding='utf-8') as stream:
                hospital = yaml.load(stream)
                if hospital['dataversion'] != version:
                    continue

                province = hospital['province']
                name = hospital['name']
                if province not in hospitals:
                    hospitals[province] = {}
                hospitals[province][name] = hospital

    # dump to json files
    dist = 'output/json'
    os.makedirs(dist, exist_ok=True)

    provinces = {}
    for province in hospitals:
        province_pinyin = "".join(lazy_pinyin(province))
        province_filename = province_pinyin + '.json'
        provinces[province] = {'json_filename': province_filename, 'pinyin': province_pinyin}
        json.dump(hospitals[province], open(dist + '/'+ province_filename, 'w'), ensure_ascii=False, indent=2)

    json.dump(provinces, open(dist + '/hospitals.json', 'w'), ensure_ascii=False, indent=2)

    # dump to HTML file
    template_dir = 'resource/templates'
    dist_dir = 'output/html'
    os.makedirs(dist, exist_ok=True)

    render_html(template_dir + '/hospitals.phtml', dist_dir + '/hospitals.html', provinces=provinces)

    for province in hospitals:
        render_html(template_dir + '/province.phtml', dist_dir + '/' + provinces[province]['pinyin'] + '.html', hospitals=hospitals[province])



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python generate.py [data version]')
    else:
        do_generate(sys.argv[1])
