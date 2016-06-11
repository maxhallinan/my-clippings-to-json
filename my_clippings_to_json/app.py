from clipping import Clipping
from codecs import BOM_UTF8
import json

BOM_LEN = len(BOM_UTF8)

highlight_options = { 'subtype': 'highlight' }
highlight = Clipping(highlight_options)

bookmark_options = { 'subtype': 'bookmark' }
bookmark = Clipping(bookmark_options)

note_options = { 'subtype': 'note' }
note = Clipping(note_options)

def remove_bom(s):
    s = str.encode(s)

    if BOM_UTF8 in s:
        s = s[BOM_LEN:]

    return s.decode()

def clean_line(line):
    line = line.rstrip()
    line = remove_bom(line)

    return line

def parse_clipping(clipping):
    clipping = list(filter(None, clipping))
    parsed = {}

    if highlight.is_type(clipping):
        parsed = highlight.parse(clipping)
    elif note.is_type(clipping):
        parsed = note.parse(clipping)
    elif bookmark.is_type(clipping):
        parsed = bookmark.parse(clipping)

    return parsed

def append_to(output_file, json_str, is_first):
    if is_first:
        output_file.write('[' + json_str)
    else:
        output_file.write(',' + json_str)

    return None

def main(input_path, output_path, start_line=0):
    clipping = []
    line_count = start_line

    with \
        open(input_path, 'r', encoding='utf-8-sig') as input_file, \
        open(output_path, 'a') as output_file:

        is_first_write = True

        for i in range(start_line):
            input_file.readline()

        for line in input_file:
            line_count += 1
            line = clean_line(line)

            if Clipping.is_end(line):
                parsed = parse_clipping(clipping)
                json_str = json.dumps(parsed)
                append_to(output_file, json_str, is_first_write)
                is_first_write = False
                clipping = []
                continue

            clipping.append(line)

        output_file.write(']')

        return line_count
