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
    'match_pattern': '/./',
    'match_group': -1,
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

default_rules = {
    'authors': author_rules,
    'body': body_rules,
    'created_at': created_at_rules,
    'location_range': line_range_rules,
    'page': page_rules,
    'title': title_rules,
    'subtype': subtype_rules,
}

class Clipping(object):
    delimiter = '=========='

    parsing_rules = default_rules

    def __init__(self, options):
        self.subtype = options['subtype']

    @staticmethod
    def is_end(line):
        return line == Clipping.delimiter

    def is_subtype(self, lines):
        sl_ind = self.parsing_rules['subtype']['line']
        line = lines[sl_ind]
        line = line.lower()
        return line.find(self.subtype) > -1

    def datestring_to_unix(self, dstr):
        frmt = '%A, %B %d, %Y %I:%M:%S %p'
        dt = datetime.strptime(dstr, frmt)
        timestamp = time.mktime(dt.timetuple())
        return int(timestamp)

    def to_value_type(self, value_type, value):
        if value_type == 'date':
            value = self.datestring_to_unix(value)
        if value_type == 'number':
            value = int(value)

        return value

    def parse_line(self, rules, line):
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
                data[i] = self.to_value_type(value_type, data[i])
        else:
            data = self.to_value_type(value_type, data)

        return data

    def get_line(self, rules, lines):
        line_ind = rules['line']
        line = ''

        if len(lines) > line_ind:
            line = lines[line_ind]

        return line

    def parse(self, lines):
        parsed = {}

        for rtype in self.parsing_rules:
            rules = self.parsing_rules[rtype]
            line = self.get_line(rules, lines)
            val = self.parse_line(rules, line)

            if val:
                parsed[rtype] = val

        return parsed
