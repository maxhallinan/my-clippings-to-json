author_rules = {
    'line': 0,
}
body_rules = {
    'line': 2,
}
datetime_rules = {
    'line': 1,
}
page_rules = {
    'line': 1,
}
title_rules = {
    'line': 0,
}
subtype_rules = {
    'line': 1,
}

default_rules = {
    'author': author_rules,
    'body': body_rules,
    'datetime': datetime_rules,
    'page': page_rules,
    'title': title_rules,
    'subtype': subtype_rules,
}

class Clipping(object):
    delimiter = '=========='

    rules = default_rules

    def __init__(self, options):
        self.subtype = options['subtype']

    @staticmethod
    def is_end(line):
        return line == Clipping.delimiter 

    def is_subtype(self, lines):
        sl_ind = self.rules['subtype']['line']
        line = lines[sl_ind]
        line = line.lower()
        return line.find(self.name) > -1

    def parse(self, lines):
        parsed = { 'subtype': self.name }
        return parsed
