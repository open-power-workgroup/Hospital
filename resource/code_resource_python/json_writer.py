import json

try:
    import helpers
    import readme_reader
except ImportError:
    from . import helpers
    from . import readme_reader


def write(info_dict):
    output = json.dumps(info_dict, ensure_ascii=False)
    helpers.write_file(filename='hospital_list.json', content=outputj)


if __name__ == '__main__':
    write(readme_reader.read())
