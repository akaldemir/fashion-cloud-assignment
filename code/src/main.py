import argparse
import sys

import mapper
import grouper
import file

PRICE_CATALOG_FILE_PATH = "../tests/test_data/pricat.csv"
MAPPINGS_FILE_PATH = "../tests/test_data/mappings.csv"
FINAL_CATALOG_FILE_PATH = "final_catalog.json"


def _parse_args(args):
    parser = argparse.ArgumentParser(description="Creates formatted catalog from price catalog and mappings")

    parser.add_argument("--price_catalog", "-p",
                        type=str,
                        default=PRICE_CATALOG_FILE_PATH
                        )
    parser.add_argument("--mappings",
                        "-m",
                        type=str,
                        default=MAPPINGS_FILE_PATH
                        )
    parser.add_argument("--output",
                        "-o",
                        type=str,
                        default=FINAL_CATALOG_FILE_PATH
                        )

    return parser.parse_args(args[1:])


def main(price_catalog_filepath, mappings_filepath, output_filepath):
    variations = file.read_price_catalog(price_catalog_filepath)
    mappings, reduce_rules = file.read_mapping(mappings_filepath)

    mapped_variations = mapper.reduce_and_map(mappings, reduce_rules, variations)
    articles = grouper.group_variations_to_articles(mapped_variations)
    catalog = grouper.level_up_variations_attributes(articles)
    catalog = grouper.level_up_articles_attributes(catalog)

    file.write_final_catalog(output_filepath, catalog)


if __name__ == '__main__':
    parsed_args = _parse_args(sys.argv)
    main(parsed_args.price_catalog, parsed_args.mappings, parsed_args.output)
