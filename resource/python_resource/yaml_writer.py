"""
This file was created by Chantisnake
This code obeys GPL V3.0 licence

this file contain only a function `write`,
which will dump the input info_dict into a yaml file into `$REPO_ROOT$/resource/API_resource/hospital_list.yml`
"""

import os
import yaml

try:
    import helpers
    import readme_reader
except ImportError:
    from . import helpers
    from . import readme_reader


def write(info_dict):
    filename = os.path.join(os.getcwd(), 'resource', 'API_resource', 'hospital_list.yml')
    helpers.write_file(filename, yaml.safe_dump(info_dict, allow_unicode=True))


if __name__ == '__main__':
    info_dict = readme_reader.read()
    write(info_dict)
