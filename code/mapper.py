from typing import List

SOURCE_TYPES, DESTINATION_TYPE, SOURCES, DESTINATION = "source_types", "destination_type", "sources", "destination"


def _reduce_and_map(mappings: List[dict], variation: dict) -> dict:
    """
    Makes reducing and mapping on single variation, based on mappings list

    Parameters
    ----------
    mappings : List[dict]
        List of mapping rules

    variation : dict
        Variation container for applying mapping rules

    Returns
    -------
    dict
        Variation container with applied mapping rules
    """
    mapped_var = {key: value for key, value in variation.items() if value}
    for mapping in mappings:
        source = [variation[source_type] for source_type in mapping[SOURCE_TYPES]]
        if mapping[SOURCES] == source:
            # Pop fields to be reduced
            for source_type in mapping[SOURCE_TYPES]:
                mapped_var.pop(source_type)
            # Add new field
            mapped_var[mapping[DESTINATION_TYPE]] = mapping[DESTINATION]
    return mapped_var


def reduce_and_map(mappings: List[dict], variations: List[dict]) -> List[dict]:
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
        mapped_reduced_variation = _reduce_and_map(mappings, variation)
        mapped_reduced_variations.append(mapped_reduced_variation)

    return mapped_reduced_variations
