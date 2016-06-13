from . import clipping
from codecs import BOM_UTF8
import json
import os

BOM_LEN = len(BOM_UTF8)

def remove_bom(s):
    s = str.encode(s)

    if BOM_UTF8 in s:
        s = s[BOM_LEN:]

    return s.decode()

def clean_line(line):
    line = line.rstrip()
    line = remove_bom(line)

    return line

def parse_clipping(lines):
    lines = list(filter(None, lines))
    parsed = None

    parsed = clipping.parse(lines)

    return parsed

def append_to(output_file, json_str, is_first):
    if is_first:
        output_file.write('[' + json_str)
    else:
        output_file.write(',' + json_str)

    return None

def main(input_path, output_path, start_line=0):
    lines = []
    line_count = start_line

    try:
        os.remove(output_path)
    except OSError:
            pass

    with \
        open(input_path, 'r', encoding='utf-8-sig') as input_file, \
        open(output_path, 'a') as output_file:


        is_first_write = True

        for i in range(start_line - 1):
            input_file.readline()

        for line in input_file:
            line_count += 1
            line = clean_line(line)

            if clipping.is_end(line):
                parsed = parse_clipping(lines)
                if parsed:
                    json_str = json.dumps(parsed)
                    append_to(output_file, json_str, is_first_write)
                    is_first_write = False
                lines = []
                continue

            lines.append(line)

        if not is_first_write:
            output_file.write(']')

        return line_count
