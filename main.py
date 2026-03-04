# BOOKBOT MAIN SOURCE FILE
#
# IMPORTS

from stats import get_word_count, character_count, sort_dict
import sys

# FUNCTIONS

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text(path))} total words")
    print("--------- Character Count -------")
    for item in sort_dict(character_count(get_book_text(path))):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
