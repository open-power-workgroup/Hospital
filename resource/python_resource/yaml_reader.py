"""
This file was created by Chantisnake
This code obeys GPL V3.0 licence

this file is currently non-functional in this project, because my initial design is unnecessarily complicated.
I keep this file here because it may comes in handy sometime in the future.
"""

import yaml

try:
    import helpers
except ImportError:
    from . import helpers


def read():
    content = ''.join(helpers.read_file('hospital_list.yml'))
    return yaml.safe_load(content)


if __name__ == '__main__':
    print(read())