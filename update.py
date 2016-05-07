"""
This file was created by Chantisnake
This code obeys GPL V3.0 licence

this file is the main of the code project, this handles two functions:
- run:
parses the readme and update all the info in `$REPO_ROOT$/resource/API_reference` (a json and a yaml format of the data)
- debug:
parse the readme in debug mode, which will write down all the process of parsing in `$REPO_ROOT$/debug.log`
this function will note update json and yaml file in `$REPO_ROOT$/resource/API_reference`.
"""

from resource.python_resource import json_writer
from resource.python_resource import yaml_writer
from resource.python_resource import readme_reader
import sys


def run():
    print('run in normal mode')
    info_dict = readme_reader.read()
    print('info read, stored in info_dict')
    yaml_writer.write(info_dict)
    print('info wrote down as yaml')
    json_writer.write(info_dict)
    print('info wrote down in resource/API_resource')
    print('all finished')


def debug():
    print('run in debug mode')
    readme_reader.debug()


if __name__ == '__main__':
    if len(sys.argv) <= 1 or sys.argv[1].lower() == 'run':
        run()
    elif sys.argv[1].lower() == 'debug':
        debug()
