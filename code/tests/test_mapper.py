import pytest

from src import mapper


@pytest.mark.parametrize("attribute, result",
                         [(("season", "winter"), ("season", "Winter")),
                          (("collection", "NW 17-18"), ("collection", "Winter Collection 2017/2018")),
                          (("article_structure_code", "4"), ("article_structure", "Boot")),
                          (("article_structure_code", "5"), ("article_structure", "Sneaker")),
                          (("color_code", "1"), ("color", "Nero"))])
def test_map_attribute(mappings, attribute, result):
    assert mapper._map_attribute(mappings, attribute) == result


@pytest.mark.parametrize("result, variation",
                         [
                             ({"article_number": "01-alper", "collection": "Winter Collection 2017/2018",
                               "size_group_code": "EU", "size_code": "36", "color": "white"},
                              {"article_number": "01-alper", "collection": "NW 17-18", "size_group_code": "EU",
                               "size_code": "36", "color": "white"}),
                             ({"article_number": "01-alper", "collection": "Winter Collection 2017/2018",
                               "size_group_code": "EU", "size_code": "37", "color": "white"},
                              {"article_number": "01-alper", "collection": "NW 17-18", "size_group_code": "EU",
                               "size_code": "37", "color": "white"}),
                             ({"article_number": "01-alper", "collection": "Winter Collection 2017/2018",
                               "size_group_code": "EU", "size_code": "38", "color": "white"},
                              {"article_number": "01-alper", "collection": "NW 17-18", "size_group_code": "EU",
                               "size_code": "38", "color": "white"}),
                             ({"article_number": "02-alper", "collection": "Winter Collection 2017/2018",
                               "size_group_code": "EU", "size_code": "38", "color": "black"},
                              {"article_number": "02-alper", "collection": "NW 17-18", "size_group_code": "EU",
                               "size_code": "38", "color": "black"}),
                             ({"article_number": "02-alper", "collection": "Winter Collection 2017/2018",
                               "size_group_code": "EU", "size_code": "39", "color": "red"},
                              {"article_number": "02-alper", "collection": "NW 17-18", "size_group_code": "EU",
                               "size_code": "39", "color": "red"}),
                             ({"article_number": "03-alper", "collection": "Winter Collection 2017/2018",
                               "size_group_code": "EU", "size_code": "39", "color": "red"},
                              {"article_number": "03-alper", "collection": "NW 17-18", "size_group_code": "EU",
                               "size_code": "39", "color": "red"})
                         ])
def test_mapper(mappings, variation, result):
    assert mapper._mapper(mappings, variation) == result


@pytest.mark.parametrize("result, variation",
                         [
                             ({"article_number": "01-alper", "collection": "NW 17-18", "size": "European size 36", "color": "white"},
                              {"article_number": "01-alper", "collection": "NW 17-18", "size_group_code": "EU",
                               "size_code": "36", "color": "white"}),
                             ({"article_number": "01-alper", "collection": "NW 17-18", "size": "European size 37", "color": "white"},
                              {"article_number": "01-alper", "collection": "NW 17-18", "size": "European size 37", "color": "white"}),
                             ({"article_number": "03-alper", "collection": "NW 17-18", "size": "European size 40", "color": "red"},
                              {"article_number": "03-alper", "collection": "NW 17-18", "size_group_code": "EU",
                               "size_code": "40", "color": "red"})
                         ])
def test_reducer(reduce_rules, result, variation):
    assert mapper._reducer(reduce_rules, variation) == result


def test_reduce_and_map(mappings, reduce_rules, variations):
    result = mapper.reduce_and_map(mappings, reduce_rules, variations)
    assert result == [{'article_number': '01-alper', 'collection': 'Winter Collection 2017/2018', 'color': 'white', 'size': 'European size 36'},
                      {'article_number': '01-alper', 'collection': 'Winter Collection 2017/2018', 'size_group_code': 'EU', 'size_code': '37', 'color': 'white'},
                      {'article_number': '01-alper', 'collection': 'Winter Collection 2017/2018', 'size_group_code': 'EU', 'size_code': '38', 'color': 'white'},
                      {'article_number': '02-alper', 'collection': 'Winter Collection 2017/2018', 'size_group_code': 'EU', 'size_code': '38', 'color': 'black'},
                      {'article_number': '02-alper', 'collection': 'Winter Collection 2017/2018', 'color': 'red', 'size': 'European size 39'},
                      {'article_number': '03-alper', 'collection': 'Winter Collection 2017/2018', 'color': 'red', 'size': 'European size 39'}]
