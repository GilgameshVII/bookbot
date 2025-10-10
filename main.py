#   Prints the contents of a txt file.
from stats import get_num_words, get_chars_dict, get_sorted_dict


def main():
    book_path = "/home/jordan/workspace/github.com/GilgameshVII/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    #chars_dict = get_chars_dict(text)
    print("============ BOOKBOT ============")
    print(f"Analyzig book found at {book_path}")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count ---------")
    get_sorted_dict(text)
    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()