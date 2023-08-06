# Coding Part


## Project Structure

Project consists of 3 main parts.
- file.py: for handling io operations
- mapper.py: for mapping, reducing purposes
- grouper.py: restructuring data


## Dependencies

1. Install Python 3.11
2. Install poetry
3. Install the dependencies using poetry:

```
poetry install
```

## Running tests

```
pytest tests/
```

## Usage

```
python -m pipe --price_catalog tests/test_data/pricat.csv \
               --mappings tests/test_data/mappings.csv \
               --output output.json
```

## Notes
* We should've preferred a framework like Apache Hadoop for Mapping/Reducing in order to make it distributed 
