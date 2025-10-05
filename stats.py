
def word_count(file_contents):
    print(f"Found {len(file_contents.split())} total words")

def character_count(file_contents):
    char_count = {}

    for char in file_contents.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print(char_count)

def sort_on(file_contents):
    return file_contents["char":"", ""]

