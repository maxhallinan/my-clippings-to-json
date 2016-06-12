# my-clippings-to-json

Format Kindle clippings ('Kindle/documents/My Clippings.txt') as JSON. 

## Installation

First install [pipsi](https://github.com/mitsuhiko/pipsi#readme).

```
pipsi install .
```

## Usage

```
my_clippings_to_json [OPTIONS] INPUT OUTPUT
```

### Arguments

#### `INPUT`

path to input file

#### `OUTPUT`

path to output file

### Options

#### `-h, --help`

show help page

#### `-s, --start INTEGER`

start at line number of input file (default: 1)

## Output

### Example

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
