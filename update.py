from resource.code_resource_python import json_writer
from resource.code_resource_python import yaml_writer
from resource.code_resource_python import readme_reader
import sys


def run():
    print('run in normal mode')
    info_dict = readme_reader.read()
    print('info read, stored in info_dict')
    yaml_writer.write(info_dict)
    print('info wrote down as yaml')
    json_writer.write(info_dict)
    print('info wrote down as info_dict')
    print('all finished')


def debug():
    print('run in debug mode')
    readme_reader.debug()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        run()
    elif sys.argv[1] == 'run':
        run()
    elif sys.argv[1] == debug():
        debug()
