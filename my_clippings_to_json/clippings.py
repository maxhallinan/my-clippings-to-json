import bookmark
from codecs import BOM_UTF8
import highlight
import json
import note

HIGHLIGHT_DELIMITER = '=========='
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

def parse_clipping(clipping):
    clipping = list(filter(None, clipping))
    parsed = {}

    return parsed

def main(input_path, output_path, start_line=0):
    clipping = []
    line_count = start_line

    with \
        open(input_path, 'r', encoding='utf-8-sig') as input_file, \
        open(output_path, 'a') as output_file:

        for i in range(start_line):
            input_file.readline()

        for line in input_file:
            line_count += 1
            line = clean_line(line)

            if line == HIGHLIGHT_DELIMITER:
                clipping.append(line)
                parsed = parse_clipping(clipping)
                json.dump(parsed, output_file)
                clipping = []
                continue

            clipping.append(line)

        return line_count
