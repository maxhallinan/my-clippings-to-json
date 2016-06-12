import configparser
from datetime import datetime
import re
import time

settings = configparser.ConfigParser()
settings.read('settings.ini')

parsing_rules = configparser.ConfigParser()
parsing_rules.read('parsing_rules.ini')

def is_end(line):
    delimiter = parsing_rules['clipping']['delimiter']
    return line == delimiter

def is_subtype(lines):
    sl_ind = int(parsing_rules['subtype']['line'])
    line = lines[sl_ind]
    line = line.lower()

    return line.find(subtype) > -1

def datestring_to_unix(dstr):
    datestring_format = parsing_rules['clipping']['datestring format']
    dt = datetime.strptime(dstr, datestring_format)
    timestamp = time.mktime(dt.timetuple())

    return int(timestamp)

def to_value_type(value_type, value):
    if value_type == 'date':
        value = datestring_to_unix(value)
    if value_type == 'number':
        value = int(value)

    return value

def format_data(rules, data):
    value_type = rules['value type']

    if 'delimiter' in rules:
        data = data.split(rules['delimiter'])
        for i in range(len(data)):
            data[i] = to_value_type(value_type, data[i])
    else:
        data = to_value_type(value_type, data)

    return data

def parse_line(rules, line):
    data = None
    pattern = rules['match pattern']

    match_groups = re.compile(pattern).findall(line)

    if match_groups:
        group = int(rules['match group'])
        data = match_groups[group]

    if data:
        data = format_data(rules, data)

    return data

def get_line(rules, lines):
    line_ind = int(rules['line'])
    line = ''

    if len(lines) > line_ind:
        line = lines[line_ind]

    return line

def parse(lines):
    parsed = {}
    fields = settings['output']['fields']
    fields = fields.split(',')
    fields = [s.strip(' ') for s in fields]

    for field in fields:
        rules = parsing_rules[field]
        line = get_line(rules, lines)
        val = parse_line(rules, line)

        if val:
            field_name = settings['field names'][field]
            parsed[field_name] = val

    return parsed
