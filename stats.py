def count_book_words(book_text):
    word_count = len(book_text.split())
    return word_count

def count_characters(book_text):
    characters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
        "æ": 0,
        "â": 0,
        "ê": 0,
        "ë": 0,
        "ô": 0,
    }

    for char, char_count in characters.items():
        characters[char] = book_text.lower().count(char)
    
    return characters

def sort_key(items):
    return items["num"]


def sort_char_count(characters):
    char_count = []

    for item in characters:
        char = item
        num = characters[item]
        char_count.append({"char": char, "num": num})

    char_count.sort(reverse=True, key=sort_key)
    return char_count

