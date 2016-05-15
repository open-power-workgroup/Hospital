import os
import sys
import datetime

import ruamel.yaml as yaml
import json

from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
from pypinyin import lazy_pinyin


def render_html(template_name, dist_file, **kwargs):
    template_dir = os.path.dirname(os.path.abspath(__file__)) + '/resource/templates'
    j2_env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)
    template = j2_env.get_template(template_name)
    html = template.render(kwargs)
    with open(dist_file, 'w') as f:
        f.write(html)


def do_generate(version):
    info = {
        'version': version,
        'date': datetime.datetime.now().strftime('%Y年%m月%d日')
    }

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

    output_dir = 'output/' + version

    # dump to json files
    dist = output_dir + '/json'
    os.makedirs(dist, exist_ok=True)

    provinces = {}
    for province in hospitals:
        province_pinyin = "".join(lazy_pinyin(province))
        province_filename = province_pinyin + '.json'
        provinces[province] = {'json_filename': province_filename, 'pinyin': province_pinyin}
        json.dump(hospitals[province], open(dist + '/'+ province_filename, 'w'), ensure_ascii=False, indent=2)

    json.dump(provinces, open(dist + '/hospitals.json', 'w'), ensure_ascii=False, indent=2)

    # dump to HTML file
    dist_dir = output_dir + '/html'
    os.makedirs(dist_dir, exist_ok=True)
    print(dist_dir)

    render_html('hospitals.phtml', dist_dir + '/hospitals.html', provinces=provinces, info=info)
    for province in hospitals:
        render_html('province.phtml', dist_dir + '/' + provinces[province]['pinyin'] + '.html', hospitals=hospitals[province], province=province, info=info)



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python generate.py [data version]')
    else:
        do_generate(sys.argv[1])
