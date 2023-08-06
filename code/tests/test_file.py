import os
import json

from src import file


def test_read_price_catalog(variations):
    result = file.read_price_catalog("test_data/pricat_mini.csv")
    assert result == variations


def test_read_mapping(mappings, reduce_rules):
    mapping_result, reduce_result = file.read_mapping("test_data/mappings_mini.csv")
    assert mapping_result == mappings
    assert reduce_result == reduce_rules


def test_write_final_catalog(tmp_path, catalog_refined):
    path = tmp_path / "catalog.json"
    path_str = os.path.abspath(path)
    file.write_final_catalog(path_str, catalog_refined)

    with path.open("r") as cat_file:
        catalog_json = json.load(cat_file)
        assert catalog_json == catalog_refined
