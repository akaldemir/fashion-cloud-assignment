import pytest


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
