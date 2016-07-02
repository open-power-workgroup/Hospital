#!/usr/bin/env python
# encoding: utf-8
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
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def run(show_error=True):
    print('run in normal mode')
    if not show_error:
        print('run in silent mode, there will be no warning and error message')
    info_dict = readme_reader.read(show_error=show_error)
    print('info read, stored in info_dict')
    yaml_writer.write(info_dict)
    print('info wrote down as yaml')
    json_writer.write(info_dict)
    print('info wrote down as json')
    print('all info write down in resource/API_resource/')
    print('all finished')


def debug():
    print('run in debug mode')
    readme_reader.debug()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        run()
    elif 'run' in sys.argv and 'debug' not in sys.argv and '--silent' not in sys.argv:
        run()
    elif 'debug' in sys.argv and 'run' not in sys.argv:
        debug()
    elif '--silent' in sys.argv and 'debug' not in sys.argv:
        run(show_error=False)
    else:
        print('input is invalid')

