from typing import List
import csv

PRICE_CATALOG_FILE_PATH = "pricat.csv"
MAPPINGS_FILE_PATH = "mappings.csv"


def get_price_catalog(filepath: str) -> (List[str], List[dict]):
    """
    Get price catalog and article header from csv file

    Parameters
    ----------
    filepath : str
        Path of price catalog file in csv format

    Returns
    -------
    (List[str], List[dict])
        Tuple containing header as list of str and article variations as list of dict
    """
    variations = []
    with open(filepath) as csvfile:
        # creating a csv reader object
        csvreader = csv.DictReader(csvfile, delimiter=";")

        # extracting header
        header = csvreader.fieldnames

        # extracting fields using header
        for variation in csvreader:
            variations.append(variation)

    return header, variations


def get_mapping(filepath: str) -> List[dict]:
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

        header = next(csvreader)

        # extracting header
        for mapping in csvreader:
            mappings.append(
                {
                    "source": mapping[0].split("|"),
                    "destination": mapping[1],
                    "source_type": mapping[2].split("|"),
                    "destination_type": mapping[3]
                }
            )
        return mappings



if __name__ == '__main__':
    header, variations = get_price_catalog(PRICE_CATALOG_FILE_PATH)
    mappings = get_mapping(MAPPINGS_FILE_PATH)
