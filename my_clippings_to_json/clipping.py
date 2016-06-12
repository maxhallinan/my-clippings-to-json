from datetime import datetime
import re
import time

author_rules = {
    'line': 0,
    'match_pattern': '\(([^)]+)\)',
    'match_group': -1,
    'value_type': 'string',
    'delimiter': ';',
}
body_rules = {
    'line': 2,
    'match_pattern': '(.*)',
    'match_group': 0,
    'value_type': 'string',
}
created_at_rules = {
    'line': 1,
    'match_pattern': '(?<=Added on )(.*)',
    'match_group': -1,
    'value_type': 'date',
}
line_range_rules = {
    'line': 1,
    'match_pattern': '(?<=Location )(.*)(?= \|)',
    'match_group': -1,
    'value_type': 'number',
    'delimiter': '-'
}
page_rules = {
    'line': 1,
    'match_pattern': '(?<=page\s)(\w+)',
    'match_group': -1,
    'value_type': 'number',
}
subtype_rules = {
    'line': 1,
    'match_pattern': '(?<=Your\s)(\w+)',
    'match_group': -1,
    'value_type': 'string',
    'lower_case': True
}
title_rules = {
    'line': 0,
    'match_pattern': '(^.*)(?=\s\()',
    'match_group': -1,
    'value_type': 'string',
}
parsing_rules = {
    'authors': author_rules,
    'body': body_rules,
    'created_at': created_at_rules,
    'location_range': line_range_rules,
    'page': page_rules,
    'title': title_rules,
    'subtype': subtype_rules,
}
delimiter = '=========='
datestring_format = '%A, %B %d, %Y %I:%M:%S %p' 

def is_end(line):

    return line == delimiter

def is_subtype(lines):
    sl_ind = parsing_rules['subtype']['line']
    line = lines[sl_ind]
    line = line.lower()

    return line.find(subtype) > -1

def datestring_to_unix(dstr):
    dt = datetime.strptime(dstr, datestring_format)
    timestamp = time.mktime(dt.timetuple())

    return int(timestamp)

def to_value_type(value_type, value):
    if value_type == 'date':
        value = datestring_to_unix(value)
    if value_type == 'number':
        value = int(value)

    return value

def parse_line(rules, line):
    data = None
    pattern = rules['match_pattern']
    value_type = rules['value_type']

    m = re.compile(pattern).findall(line)

    if m:
        group = rules['match_group']
        data = m[group]

    if not data:
        return None

    if 'delimiter' in rules:
        data = data.split(rules['delimiter'])
        for i in range(len(data)):
            data[i] = to_value_type(value_type, data[i])
    else:
        data = to_value_type(value_type, data)

    return data

def get_line(rules, lines):
    line_ind = rules['line']
    line = ''

    if len(lines) > line_ind:
        line = lines[line_ind]

    return line

def parse(lines):
    parsed = {}

    for rtype in parsing_rules:
        rules = parsing_rules[rtype]
        line = get_line(rules, lines)
        val = parse_line(rules, line)

        if val:
            parsed[rtype] = val

    return parsed
