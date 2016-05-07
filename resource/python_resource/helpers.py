"""
This file was created by Chantisnake
This code obeys GPL V3.0 licence

this file is the helpers for this project,
which includes the constants and general function(functions that are used cross file)
"""

# -----------------------------------------------------
# CONSTANTS
# -----------------------------------------------------
HOSPITAL_LIST_BEGIN_SYMBOL = "[](hospital list begin //PLEASE DO NOT DELETE THIS LINE)"
HOSPITAL_LIST_END_SYMBOL = "[](hospital list end //PLEASE DO NOT DELETE THIS LINE)"
CHINESE_REGEX_WITH_NUM_LETTER = r'[\u4e00-\u9fffA-Za-z0-9.():/?=%]+'

FILE_WRITE_ERROR = '''file cannot be created
the input file name is {}
if you do not understand the message, please open a new issue at:
https://github.com/open-power-workgroup/Hospital/issues'''

FILE_READ_ERROR = '''the file cannot be found please make sure that you have correct file name inputted'
the input file name is {}
if you do not understand the message, please open a new issue at:
https://github.com/open-power-workgroup/Hospital/issues'''


# -----------------------------------------------------
# GENERAL FUNCTIONS
# -----------------------------------------------------
def read_file(filename):
    """
    read the file and handle exceptions
    :param filename: the file name of the file that you want to read
    :return: if the file exist, will return a list of string, each string is one line in the read me file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()

    except IOError:  # file don't exist
        print(FILE_READ_ERROR.format(filename))


def write_file(filename, content):
    """
    write a string to a file and handle exceptions
    :param filename: the file name of the file that you want to write to
    :param content: the content you want to write to this file
    :return: if the file exist, will return a list of string, each string is one line in the read me file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

    except IOError:  # file don't exist
        print(FILE_WRITE_ERROR.format(filename))


def write_log(*args):
    log_name = 'debug.log'
    string_args = [str(arg) for arg in args]
    line = ' '.join(string_args).rstrip() + '\n'
    try:
        with open(log_name, 'a', encoding='utf-8') as f:
            f.write(line)
    except IOError:
        print(FILE_WRITE_ERROR.format(log_name))
