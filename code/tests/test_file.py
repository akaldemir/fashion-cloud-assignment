import os
import json

from src import file


def test_read_price_catalog(variations):
    result = file.read_price_catalog("test_data/pricat_mini.csv")
    assert result == variations


def test_read_mapping():
    mappings, reduce_rules = file.read_mapping("test_data/mappings_mini.csv")
    assert mappings == [
        {'sources': 'winter', 'destination': 'Winter', 'source_types': 'season', 'destination_type': 'season'},
        {'sources': 'NW 17-18', 'destination': 'Winter Collection 2017/2018', 'source_types': 'collection', 'destination_type': 'collection'},
        {'sources': '4', 'destination': 'Boot', 'source_types': 'article_structure_code', 'destination_type': 'article_structure'},
        {'sources': '5', 'destination': 'Sneaker', 'source_types': 'article_structure_code', 'destination_type': 'article_structure'},
        {'sources': '1', 'destination': 'Nero', 'source_types': 'color_code', 'destination_type': 'color'}
    ]
    assert reduce_rules == [
        {'sources': ['EU', '36'], 'destination': 'European size 36', 'source_types': ['size_group_code', 'size_code'], 'destination_type': 'size'},
        {'sources': ['EU', '40'], 'destination': 'European size 40', 'source_types': ['size_group_code', 'size_code'], 'destination_type': 'size'},
    ]


def test_write_final_catalog(tmp_path, catalog_refined):
    path = tmp_path / "catalog.json"
    path_str = os.path.abspath(path)
    file.write_final_catalog(path_str, catalog_refined)

    with path.open("r") as cat_file:
        catalog_json = json.load(cat_file)
        assert catalog_json == catalog_refined
