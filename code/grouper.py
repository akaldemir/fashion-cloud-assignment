from typing import List

from toolz import itertoolz

ARTICLES, ARTICLE_NUMBER, VARIATIONS = "articles", "article_number", "variations"


def group_variations_to_articles(variations: List[dict]) -> List[dict]:
    """
    Groups variations based on the article numbers

    Parameters
    ----------
    variations : List[dict]
        List of variations

    Returns
    -------
    List[dict]
        List of articles with corresponding article number and variations
    """
    articles_dict = itertoolz.groupby(ARTICLE_NUMBER, variations)
    articles = [{ARTICLE_NUMBER: article_number, VARIATIONS: variation_list} for article_number, variation_list in articles_dict.items()]
    return articles


def _level_up_attributes(main_container: dict, child_name: str, exclude_key: str | None = None) -> dict:
    """
    Levels up attributes in child containers if they're sharing the same value

    Parameters
    ----------
    main_container : dict
        Main container which holds all the child containers and attributes

    child_name : str
        Name of the child container

    exclude_key : str | None
        Key to exclude from attributes to level up

    Returns
    -------
    dict
        Container with updated attributes
    """
    # Store keys in a list as Python doesn't let size change during iteration
    child_container = main_container[child_name]
    keys = [key for key in child_container[0].keys() if key != exclude_key]
    for key in keys:
        # Store values for a certain key in a set to check if there is only one option or not
        values = {variation[key] for variation in child_container}
        if len(values) == 1:
            # Add attribute to main container(leveling up)
            main_container[key] = values.pop()
            # Pop attribute from child container which is already leveled up
            for v in child_container:
                v.pop(key)
    return main_container


def level_up_variations_attributes(articles: List[dict]) -> dict:
    """
    Levels up attributes of variations to article level

    Parameters
    ----------
    articles : List[dict]
        List of articles which will be searched for leveling up their articles

    Returns
    -------
    dict
        Catalog containing list of articles with updated attributes
    """
    # Levels up variation attributes for every article
    for article in articles:
        _level_up_attributes(article, VARIATIONS)
    catalog = {ARTICLES: articles}
    return catalog


def level_up_articles_attributes(catalog: dict) -> dict:
    """
    Levels up attributes of articles

    Parameters
    ----------
    catalog : dict
        Catalog which will be searched for leveling up attributes of articles

    Returns
    -------
    dict
        Catalog with updated attributes
    """
    # Levels up article attributes
    return _level_up_attributes(catalog, ARTICLES, VARIATIONS)
