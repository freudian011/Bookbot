from stats import (
    get_num_words,
    get_chars_dict,
    sort_on,
    chars_dict_to_sorted_list,
)

def test_get_num_words():
    result = get_num_words("hello world")
    assert result == 2

def test_get_num_words_empty():
    result = get_num_words("")
    assert result == 0

def test_get_chars_dict():
    result = get_chars_dict("hello")
    assert result == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1,
    }

def test_get_chars_dict_uppercase():
    result = get_chars_dict("Hello")
    assert result == {
        "h": 1,
        "e": 1,
        "l": 2,
        "o": 1,
    }

def test_sort_on():
    result = sort_on(("a", 15))
    assert result == 15

def test_chars_dict_to_sorted_list():
    result = chars_dict_to_sorted_list({
        "a": 5,
        "b": 2,
        "c": 8,
    })
    assert result == [
        ("c", 8),
        ("a", 5),
        ("b", 2),
    ]
