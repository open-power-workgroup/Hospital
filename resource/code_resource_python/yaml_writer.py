import yaml
try:
    import readme_reader
except ImportError:
    from . import readme_reader
import helpers


def write(info_dict):
    helpers.write_file('hospital_list.yml', yaml.safe_dump(info_dict, allow_unicode=True))


if __name__ == '__main__':
    info_dict = readme_reader.parse()
    write(info_dict)
