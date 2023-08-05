import argparse

import pytest

import main as main


PRICE_CATALOG_FILE_PATH = "/some_path/some_price.csv"
MAPPINGS_FILE_PATH = "/some_path/some_mapping.csv"
FINAL_CATALOG_FILE_PATH = "/some_path/output.json"


@pytest.fixture
def command_line_arguments():
    return argparse.Namespace(price_catalog=PRICE_CATALOG_FILE_PATH, mappings=MAPPINGS_FILE_PATH, output=FINAL_CATALOG_FILE_PATH)


def test_parse_args(command_line_arguments):
    assert main._parse_args(["main.py",
                             "-p", PRICE_CATALOG_FILE_PATH,
                             "-m", MAPPINGS_FILE_PATH,
                             "-o", FINAL_CATALOG_FILE_PATH]
                            ) == command_line_arguments


# def test_main(mocker):
#     read_price_mocker = mocker.patch("file.read_price_catalog")
#     read_map_mocker = mocker.patch("file.read_mapping")
#
#     mapper_mock = mocker.patch("mapper.reduce_and_map")
#     group_mock = mocker.patch("grouper.group_variations_to_articles")
#     level_var_mock = mocker.patch("grouper.level_up_variations_attributes")
#     level_article_mock = mocker.patch("grouper.level_up_articles_attributes")
#     level_article_mock = mocker.patch("file.write_final_catalog")
#
#     main.main(PRICE_CATALOG_FILE_PATH, MAPPINGS_FILE_PATH, FINAL_CATALOG_FILE_PATH)
#
#     read_price_mocker.assert_called_with(PRICE_CATALOG_FILE_PATH)