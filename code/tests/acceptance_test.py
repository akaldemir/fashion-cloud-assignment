import json

from src.main import main


def test_acceptance():
    main("test_data/pricat.csv",
         "test_data/mappings.csv",
         "test_data/test_catalog.json"
         )
    with open("test_data/test_catalog.json", "r") as catalog_test_file:
        test_catalog_json = json.load(catalog_test_file)
        with open("test_data/final_catalog.json", "r") as catalog_file:
            catalog_json = json.load(catalog_file)

            assert catalog_json == test_catalog_json
