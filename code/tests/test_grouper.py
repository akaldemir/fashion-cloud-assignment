import pytest

from src import grouper


@pytest.fixture
def articles_with_article_number_in_variations():
    articles = [
        {
            "article_number": "01-alper",
            "variations": [
                {"article_number": "01-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "36",
                 "color": "white"},
                {"article_number": "01-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "37",
                 "color": "white"},
                {"article_number": "01-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "38",
                 "color": "white"}],
        },
        {
            "article_number": "02-alper",
            "variations": [
                {"article_number": "02-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "38",
                 "color": "black"},
                {"article_number": "02-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "39",
                 "color": "red"}],
        },
        {
            "article_number": "03-alper",
            "variations": [
                {"article_number": "03-alper", "collection": "NW 17-18", "size_group_code": "EU", "size_code": "39",
                 "color": "red"}],
        },
    ]
    return articles


@pytest.fixture
def catalog_unrefined():
    catalog = {
        "articles": [
            {
                "article_number": "01-alper",
                "collection": "NW 17-18",
                "size_group_code": "EU",
                "color": "white",
                "variations": [
                    {"size_code": "36"},
                    {"size_code": "37"},
                    {"size_code": "38"}
                ],
            },
            {
                "article_number": "02-alper",
                "collection": "NW 17-18",
                "size_group_code": "EU",
                "variations": [
                    {"size_code": "38", "color": "black"},
                    {"size_code": "39", "color": "red"}],
            },
            {
                "article_number": "03-alper",
                "collection": "NW 17-18",
                "size_group_code": "EU",
                "size_code": "39",
                "color": "red",
                "variations": [{}],
            },
        ]
    }
    return catalog


def test_group_variations_to_articles(variations, articles_with_article_number_in_variations):
    articles = grouper.group_variations_to_articles(variations)
    # "article_number" inside the variations attribute will be ommitted by level up function.
    assert articles == articles_with_article_number_in_variations


def test_level_up_variations_attributes(articles_with_article_number_in_variations, catalog_unrefined):
    catalog = grouper.level_up_variations_attributes(articles_with_article_number_in_variations)

    assert catalog == catalog_unrefined


def test_level_up_articles_attributes(catalog_unrefined, catalog_refined):
    result = grouper.level_up_articles_attributes(catalog_unrefined)

    assert result == catalog_refined
