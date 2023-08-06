import argparse

import pytest

from src import main as main

PRICE_CATALOG_FILE_PATH = "/some_path/some_price.csv"
MAPPINGS_FILE_PATH = "/some_path/some_mapping.csv"
FINAL_CATALOG_FILE_PATH = "/some_path/output.json"


@pytest.fixture
def command_line_arguments():
    return argparse.Namespace(price_catalog=PRICE_CATALOG_FILE_PATH,
                              mappings=MAPPINGS_FILE_PATH,
                              output=FINAL_CATALOG_FILE_PATH
                              )


@pytest.fixture
def command_line_arguments_for_argless():
    return argparse.Namespace(price_catalog="../tests/test_data/pricat.csv",
                              mappings="../tests/test_data/mappings.csv",
                              output="final_catalog.json"
                              )


def test_parse_args(command_line_arguments):
    assert main._parse_args(["main.py",
                             "-p", PRICE_CATALOG_FILE_PATH,
                             "-m", MAPPINGS_FILE_PATH,
                             "-o", FINAL_CATALOG_FILE_PATH]
                            ) == command_line_arguments


def test_parse_args_without_args(command_line_arguments_for_argless):
    assert main._parse_args(["main.py"]) == command_line_arguments_for_argless


def test_main(mocker):
    read_price_mocker = mocker.patch("file.read_price_catalog", return_value="some_variations")
    read_map_mocker = mocker.patch("file.read_mapping", return_value=("some_mappings", "some_reduce_rules"))

    mapper_mock = mocker.patch("mapper.reduce_and_map", return_value="some_mapped")
    group_mock = mocker.patch("grouper.group_variations_to_articles", return_value="some_Articles")
    level_var_mock = mocker.patch("grouper.level_up_variations_attributes", return_value="some_catalog")
    level_article_mock = mocker.patch("grouper.level_up_articles_attributes", return_value="some_catalog2")
    write_final_mock = mocker.patch("file.write_final_catalog", return_value="some_catalog")

    main.main(PRICE_CATALOG_FILE_PATH, MAPPINGS_FILE_PATH, FINAL_CATALOG_FILE_PATH)

    read_price_mocker.assert_called_with(PRICE_CATALOG_FILE_PATH)
    read_map_mocker.assert_called_with(MAPPINGS_FILE_PATH)

    mapper_mock.assert_called_with("some_mappings", "some_reduce_rules", "some_variations")
    group_mock.assert_called_with("some_mapped")
    level_var_mock.assert_called_with("some_Articles")
    level_article_mock.assert_called_with("some_catalog")

    write_final_mock.assert_called_with(FINAL_CATALOG_FILE_PATH, "some_catalog2")
