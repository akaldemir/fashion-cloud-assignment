from typing import List
import json
import csv


def read_price_catalog(filepath: str) -> List[dict]:
    """
    Get price catalog and article header from csv file

    Parameters
    ----------
    filepath : str
        Path of price catalog file in csv format

    Returns
    -------
    List[dict]
        Article variations as list of dict
    """
    variations = []
    with open(filepath) as csvfile:
        # creating a csv reader object
        csvreader = csv.DictReader(csvfile, delimiter=";")

        # extracting fields using header
        for variation in csvreader:
            variations.append(variation)

    return variations


def read_mapping(filepath: str) -> List[dict]:
    """
    Get mapping data from csv file

    Parameters
    ----------
    filepath : str
        Path of price catalog file in csv format

    Returns
    -------
    List[dict]
        List of mappings in dict format
    """
    mappings = []
    with open(filepath) as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile, delimiter=";")

        next(csvreader)

        # extracting header
        for mapping in csvreader:
            mappings.append(
                {
                    "sources": mapping[0].split("|"),
                    "destination": mapping[1],
                    "source_types": mapping[2].split("|"),
                    "destination_type": mapping[3]
                }
            )
        return mappings


def write_final_catalog(filepath: str, catalog: dict):
    """
    Writes catalog to file

    Parameters
    ----------
    filepath : str
        Path of catalog file to write in json format

    catalog : dict
        Container to be used for writing
    """
    with open(filepath, "w") as file:
        json.dump(catalog, file, indent=2)
