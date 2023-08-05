import argparse
import sys

import grouper
import mapper
import file

PRICE_CATALOG_FILE_PATH = "pricat.csv"
MAPPINGS_FILE_PATH = "mappings.csv"
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

    return parser.parse_args()


def main(price_catalog_filepath, mappings_filepath, output_filepath):
    header, variations = file.read_price_catalog(price_catalog_filepath)
    mappings = file.read_mapping(mappings_filepath)

    mapped_variations = mapper.reduce_and_map(mappings, variations)
    articles = grouper.group_variations_to_articles(mapped_variations)
    catalog = grouper.level_up_variations_attributes(articles)
    catalog = grouper.level_up_articles_attributes(catalog)

    file.write_final_catalog(output_filepath, catalog)


if __name__ == '__main__':
    args = _parse_args(sys.argv)
    main(args.price_catalog, args.mappings, args.output)
