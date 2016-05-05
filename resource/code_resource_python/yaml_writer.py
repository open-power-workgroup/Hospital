import yaml
try:
    import helpers
    import readme_reader
except ImportError:
    from . import helpers
    from . import readme_reader


def write(info_dict):
    helpers.write_file('hospital_list.yml', yaml.safe_dump(info_dict, allow_unicode=True))


if __name__ == '__main__':
    info_dict = readme_reader.read()
    write(info_dict)
