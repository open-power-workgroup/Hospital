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
