import sys
from stats import count_book_words
from stats import count_characters
from stats import sort_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content
    
def main():
    filepath = ""
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]


    book_text = get_book_text(filepath)
    num_words = count_book_words(book_text)
    characters = count_characters(book_text)
    char_count = sort_char_count(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_count:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    


main()