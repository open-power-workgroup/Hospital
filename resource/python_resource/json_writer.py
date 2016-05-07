"""
This file was created by Chantisnake
This code obeys GPL V3.0 licence

this file contain only a function `write`,
which will dump the input info_dict into a json file into `$REPO_ROOT$/resource/API_resource/hospital_list.json`
"""

import json
import os

try:
    import helpers
    import readme_reader
except ImportError:
    from . import helpers
    from . import readme_reader


def write(info_dict):
    filename = os.path.join(os.getcwd(), 'resource', 'API_resource', 'hospital_list.json')
    output = json.dumps(info_dict, ensure_ascii=False, indent=2)
    helpers.write_file(filename=filename, content=output)


if __name__ == '__main__':
    write(readme_reader.read())
