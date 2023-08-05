import grouper
import mapper
import file

PRICE_CATALOG_FILE_PATH = "pricat.csv"
MAPPINGS_FILE_PATH = "mappings.csv"
FINAL_CATALOG_FILE_PATH = "final_catalog.json"


if __name__ == '__main__':
    header, variations = file.read_price_catalog(PRICE_CATALOG_FILE_PATH)
    mappings = file.read_mapping(MAPPINGS_FILE_PATH)

    mapped_variations = mapper.reduce_and_map(mappings, variations)
    print(mapped_variations)
    articles = grouper.group_variations_to_articles(mapped_variations)
    print(articles)
    catalog = grouper.level_up_variations_attributes(articles)
    catalog = grouper.level_up_articles_attributes(catalog)

    file.write_final_catalog(FINAL_CATALOG_FILE_PATH, catalog)
