def get_num_words(text: str) -> int:
    """Counts the total number of words in the text."""
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str, int]:
    """Counts how many times each lowercase letter appears in the text."""
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(char_count: tuple[str, int]) -> int:
    """Helper function to tell Python to sort by the character count value."""
    return char_count[1]


def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    """Turns the character dictionary into a list sorted from highest to lowest count."""
    chars_list: list[tuple[str, int]] = []
    for char in num_chars_dict:
        count = num_chars_dict[char]
        chars_list.append((char, count))
    return sorted(chars_list, reverse=True, key=sort_on)