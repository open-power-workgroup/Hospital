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
    output = json.dumps(info_dict, ensure_ascii=False)
    helpers.write_file(filename=filename, content=output)


if __name__ == '__main__':
    write(readme_reader.read())
