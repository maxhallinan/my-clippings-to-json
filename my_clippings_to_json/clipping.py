import re

author_rules = {
    'line': 0,
    'match': '',
    'value_type': 'string',
}
body_rules = {
    'line': 2,
    'match': '',
    'value_type': 'string',
}
datetime_rules = {
    'line': 1,
    'match': '',
    'value_type': 'date',
}
line_range_rules = {
    'line': 0,
    'match': '',
    'value_type': 'number',
    'delimiter': '-'
}
page_rules = {
    'line': 1,
    'match': '',
    'value_type': 'number',
}
subtype_rules = {
    'line': 1,
    'value_type': 'string',
    'to_lower': True
}
title_rules = {
    'line': 0,
    'match': '',
    'value_type': 'string',
}

default_rules = {
    'authors': author_rules,
    'body': body_rules,
    'created_on': datetime_rules,
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

    def to_value_type(self, value_type, value):
        if value_type == 'date':
            return value
        if value_type == 'number':
            return int(value)

        return value

    def format_line(self, rules, line):
        if rules.to_lower:
            line = line.lower()
        return line

    def parse_line(self, rules, line):
        return line

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
