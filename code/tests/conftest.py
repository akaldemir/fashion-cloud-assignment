import pytest


@pytest.fixture
def mappings():
    mappings = [
        {'sources': 'winter', 'destination': 'Winter', 'source_types': 'season', 'destination_type': 'season'},
        {'sources': 'NW 17-18', 'destination': 'Winter Collection 2017/2018', 'source_types': 'collection', 'destination_type': 'collection'},
        {'sources': '4', 'destination': 'Boot', 'source_types': 'article_structure_code', 'destination_type': 'article_structure'},
        {'sources': '5', 'destination': 'Sneaker', 'source_types': 'article_structure_code', 'destination_type': 'article_structure'},
        {'sources': '1', 'destination': 'Nero', 'source_types': 'color_code', 'destination_type': 'color'}
    ]
    return mappings


@pytest.fixture
def reduce_rules():
    reduce_rules = [
        {'sources': ['EU', '36'], 'destination': 'European size 36', 'source_types': ['size_group_code', 'size_code'], 'destination_type': 'size'},
        {'sources': ['EU', '39'], 'destination': 'European size 39', 'source_types': ['size_group_code', 'size_code'], 'destination_type': 'size'},
        {'sources': ['EU', '40'], 'destination': 'European size 40', 'source_types': ['size_group_code', 'size_code'], 'destination_type': 'size'},
    ]
    return reduce_rules


@pytest.fixture
def variations():
    variations = [
        {"article_number": "01-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "36", "color": "white"},
        {"article_number": "01-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "37", "color": "white"},
        {"article_number": "01-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "38", "color": "white"},
        {"article_number": "02-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "38", "color": "black"},
        {"article_number": "02-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "39", "color": "red"},
        {"article_number": "03-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "39", "color": "red"},
    ]
    return variations


@pytest.fixture
def catalog_refined():
    catalog = {
        "collection": "NW 17-18",
        "size_group_code": "EU",
        "articles": [
            {
                "article_number": "01-alper",
                "color": "white",
                "variations": [
                    {"size_code": "36"},
                    {"size_code": "37"},
                    {"size_code": "38"}
                ],
            },
            {
                "article_number": "02-alper",
                "variations": [
                    {"size_code": "38", "color": "black"},
                    {"size_code": "39", "color": "red"}],
            },
            {
                "article_number": "03-alper",
                "size_code": "39",
                "color": "red",
                "variations": [{}],
            },
        ]
    }
    return catalog
