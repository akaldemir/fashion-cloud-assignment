from typing import List

SOURCE_TYPES, DESTINATION_TYPE, SOURCES, DESTINATION = "source_types", "destination_type", "sources", "destination"


def _map_attribute(mappings: List[dict], variation_attribute: tuple) -> tuple:
    """
    Maps single attribute of a variation, based on mappings list

    Parameters
    ----------
    mappings : List[dict]
        List of mapping rules

    variation_attribute : tuple
        Variation attributes key and value in tuple format

    Returns
    -------
    tuple
        Mapped attributes key and value in tuple format
    """
    for mapping in mappings:
        if mapping[SOURCE_TYPES] == variation_attribute[0] and mapping[SOURCES] == variation_attribute[1]:
            return mapping[DESTINATION_TYPE], mapping[DESTINATION]
    return variation_attribute[0], variation_attribute[1]


def _mapper(mappings: List[dict], variation: dict) -> dict:
    """
    Maps variation attributes, based on mappings list

    Parameters
    ----------
    mappings : List[dict]
        List of mapping rules

    variation : dict
        Variation container with random attributes

    Returns
    -------
    tuple
        Variation with mapped attributes
    """
    return dict(map(lambda pair: _map_attribute(mappings, pair), variation.items()))


def _reducer(reduce_rules: List[dict], variation: dict) -> dict:
    """
    Reduces variation attributes, based on mappings list

    Parameters
    ----------
    reduce_rules : List[dict]
        List of reducing rules

    variation : dict
        Variation container with random attributes

    Returns
    -------
    tuple
        Variation with reduced attributes
    """
    # Eliminates blank fields with if statement inside of dict comprehension
    mapped_var = {key: value for key, value in variation.items() if value}
    for reduce_rule in reduce_rules:
        source = [variation[source_type] for source_type in reduce_rule[SOURCE_TYPES]]
        if reduce_rule[SOURCES] == source:
            # Pop fields to be reduced
            for source_type in reduce_rule[SOURCE_TYPES]:
                mapped_var.pop(source_type)
            # Add new field
            mapped_var[reduce_rule[DESTINATION_TYPE]] = reduce_rule[DESTINATION]
    return mapped_var


def reduce_and_map(mappings: List[dict], reduce_rules: List[dict], variations: List[dict]) -> List[dict]:
    """
    Makes reducing and mapping on all variations, based on mappings list

    Parameters
    ----------
    mappings : List[dict]
        List of mapping rules

    variations : List[dict]
        List of variation containers for applying mapping rules

    Returns
    -------
    List[dict]
        List of variation container with applied mapping rules
    """
    mapped_reduced_variations = []

    for variation in variations:
        mapped_variation = _mapper(mappings, variation)
        mapped_reduced_variation = _reducer(reduce_rules, mapped_variation)

        mapped_reduced_variations.append(mapped_reduced_variation)

    return mapped_reduced_variations
