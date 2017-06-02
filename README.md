# my-clippings-to-json

Format 'Kindle/documents/My Clippings.txt' as JSON. 

## Example

```json
[{
  "body": "in certain contexts at least, the transparency of open code should be a requirement.",
  "created_at": 1462434461,
  "title": "Code version 2.0",
  "subtype": "Highlight",
  "page": 143,
  "authors": ["Lessig, Lawrence"],
  "location_range": [2618, 2619]
}]
```

## Installation

First install [pipsi](https://github.com/mitsuhiko/pipsi#readme).

```
pipsi install .
```

## Usage

```
my-clippings-to-json [OPTIONS] INPUT_PATH OUTPUT_PATH
```

### Arguments

#### `INPUT_PATH`

Path to input file.

#### `OUTPUT_PATH`

Path to output file.

File existing at `OUTPUT_PATH` will be overwritten.

### Options

#### `-h, --help`

Show help page.

#### `-s, --start INTEGER`

Start at line number of input file (default: 1).

`INTEGER` should be the first line of the target clipping or the last line of the
preceding clipping. If `INTEGER` falls in the middle of a clipping, that clipping 
will be skipped. 

`my-clippings-to-json` writes the last line number to `stdout`. Next time, start at 
this line number.
