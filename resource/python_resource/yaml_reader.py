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