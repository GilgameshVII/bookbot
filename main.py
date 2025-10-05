#   Prints the contents of a txt file.

from stats import word_count, character_count, sort_on


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)
        word_count(file_contents)
        character_count(file_contents)

    
def main():
    get_book_text("/home/jordan/workspace/github.com/GilgameshVII/books/frankenstein.txt")

main()