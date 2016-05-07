"""
This file was created by Chantisnake
This code obeys GPL V3.0 licence

this file provides series of functions to parse and read the README
and will return a dictionary object with all the information in the readme
you know, dictionary, so make sure you computer has enough memory (if one day we really have thousands of data)

the dictionary will of this form:
{
    <city1>:
    {
        <hospital1>:
        {
            <info1>: [<info_detail1>, <info_detail2>]
            <info2>: [<info_detail>,]
            <info3>: []
        }
        <hospital2>:
        {}
    }
    <city2>:
    {
        <hospital1>:
        {}
    }

}
"""
import json
import os
import re

try:
    import helpers
except ImportError:
    from . import helpers


def __parse_city__(city_line=""):
    """
    parse the line of the city
    :param city_line: the line that contain city information
    :return the name of the city
    """
    # first find all the chinese character, and concatenate all of them
    return "".join(re.findall(helpers.CHINESE_REGEX_WITH_NUM_LETTER, city_line))


def __parse_hospital__(hospital_line=""):
    # first find all the chinese character, and concatenate all of them
    return "".join(re.findall(helpers.CHINESE_REGEX_WITH_NUM_LETTER, hospital_line))


def __parse_hospital_info__(info_line=""):
    info_list = re.findall(helpers.CHINESE_REGEX_WITH_NUM_LETTER, info_line)
    key = info_list[0]
    try:
        value = "".join(info_list[1:])
        return key, value
    except IndexError:
        return key, []


def __get_leading_space_num__(line=""):
    return len(line) - len(line.lstrip(' '))


def __get_info_line_num__(content_lines=('',)):
    forward_index = 0
    backward_index = -1

    while not content_lines[forward_index].startswith(helpers.HOSPITAL_LIST_BEGIN_SYMBOL):
        forward_index += 1
    while not content_lines[backward_index].startswith(helpers.HOSPITAL_LIST_END_SYMBOL):
        backward_index -= 1

    forward_index += 1
    backward_index -= 1
    return forward_index, backward_index


def __parse_all__(content_lines=("",), debug_mode=False):
    # init variable
    prev_leading_space_num = 0  # this is the number of leading white space in the previous line
    prev_type_index = 0  # this is the type index of the previous line(see helpers.TYPE_MAP for more)
    cur_city = ""  # this is the current city at the point we are parsing
    cur_hospital = ""  # this is the current hospital that we are parsing
    info_dict = {}  # the return variable that contain all the

    # calculation
    for content_line in content_lines:
        if not content_line.isspace():  # if this line is not space

            if debug_mode:
                helpers.write_log('')
                helpers.write_log('this is the current line we are processing:')
                helpers.write_log(content_line)

            # it is a title, which means this is a city
            if content_line.startswith('#'):
                parsed_line = __parse_city__(content_line)
                if debug_mode:
                    helpers.write_log('this is a city line')
                if parsed_line == '':
                    print('we encounter a warning while parsing readme: ')
                    print('this line will be parsed as empty:')
                    print(content_line[:-1])
                    print('we will not add this line to the result')
                    if debug_mode:
                        helpers.write_log('WARNING: this line contains illegal string, that will parse as empty')
                    else:
                        print('you can run program in debug mode for further information')
                else:
                    info_dict.update({parsed_line: {}})
                    cur_city = parsed_line
            else:
                # determine the type of information of this line
                cur_leading_space_num = __get_leading_space_num__(content_line)
                if cur_leading_space_num == prev_leading_space_num:
                    cur_type_index = prev_type_index
                elif cur_leading_space_num < prev_leading_space_num:
                    cur_type_index = prev_type_index - 1
                else:
                    cur_type_index = prev_type_index + 1

                # parse the current line into the info_dict
                # this line is a hospital
                if cur_type_index == 0:
                    parsed_line = __parse_hospital__(content_line)
                    if parsed_line == '':
                        print('we encounter a warning while parsing readme: ')
                        print('this line will be parsed as empty:')
                        print('"' + content_line[:-1] + '"')
                        print('we will not add this line to the result')
                        if debug_mode:
                            helpers.write_log('WARNING: this line contains illegal string, that will parse as empty')
                        else:
                            print('you can run program in debug mode for further information')
                    else:
                        info_dict[cur_city].update({parsed_line: {}})
                        cur_hospital = parsed_line
                # this is a info line
                elif cur_type_index == 1:
                    key, value = __parse_hospital_info__(content_line)
                    try:
                        if value in info_dict[cur_city][cur_hospital][key]:  # key in info dict and value duplicated
                            print('we encounter a warning will parsing readme:')
                            print('this line is a duplicate info of previous info')
                            print('"' + content_line[:-1] + '"')
                            print('the hospital is', cur_hospital)
                            print('the city is', cur_city)
                            if debug_mode:
                                helpers.write_log(
                                    'WARNING: this line is a duplicate of info')
                            else:
                                print('you can run program in debug mode for further information')
                        else:  # key in info dict and value not duplicated
                            info_dict[cur_city][cur_hospital][key].append(value)
                    except KeyError:  # key not in info dict
                        info_dict[cur_city][cur_hospital][key] = [value, ]
                else:
                    print('we cannot recognize the type of the line')
                    print('here is some information you can send to the issue:')
                    print('    this is the line')
                    print('   ', "'" + content_line[:-1] + "'")
                    print('    previous line has', prev_leading_space_num, 'leading white spaces')
                    print('    current line has', cur_leading_space_num, 'leading white spaces')
                    input('press <enter> to continue')
                    if debug_mode:
                        helpers.write_log('we cannot recognize the type of the line')
                        helpers.write_log('here is some information you can send to the issue:')
                        helpers.write_log('    this is the line')
                        helpers.write_log('   ', "'" + content_line[:-1] + "'")
                        helpers.write_log('    previous line has', prev_leading_space_num, 'leading white spaces')
                        helpers.write_log('    current line has', cur_leading_space_num, 'leading white spaces')

                # update all the previous variable for the next round
                prev_type_index = cur_type_index
                prev_leading_space_num = cur_leading_space_num
                if debug_mode:
                    helpers.write_log('the current line has', cur_leading_space_num, 'leading white space')
                    helpers.write_log('the current line has type index of', cur_type_index)

    print('parse all finished')
    if debug_mode:
        helpers.write_log()
        helpers.write_log('here is a json of the output: ')
        helpers.write_log(json.dumps(info_dict, ensure_ascii=False, sort_keys=True, indent=4))
    return info_dict


def read():
    lines = helpers.read_file('README.md')
    start, end = __get_info_line_num__(lines)
    info_dict = __parse_all__(lines[start:end])
    return info_dict


def debug():
    # try to remove debug file
    try:
        os.remove('debug.log')
    except:
        pass
    lines = helpers.read_file('README.md')
    print('reading file finished')
    start, end = __get_info_line_num__(lines)
    print()
    print('got the start and end position of hospital list')
    print('start is :', start)
    print('end is:', end)
    print('parsing started, this can take a while, please wait')
    info_dict = __parse_all__(lines[start:end], debug_mode=True)
    print('debug finished, see the log on debug.log')
    return info_dict


if __name__ == '__main__':
    print(read())
