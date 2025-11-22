def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content
    
from stats import count_book_words
from stats import count_characters

def main():
    filepath = "books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = count_book_words(book_text)
    characters = count_characters(book_text)
    char_count = list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count.sort(reverse=True)
    print(char_count)


main()