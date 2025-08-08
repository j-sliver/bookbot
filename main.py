import sys
from stats import get_num_words, get_char_count, sorted_dict

def get_book_txt(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_txt(sys.argv[1])
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(text)} total words")
        print("--------- Character Count -------")
        char_dict = get_char_count(text)
        char_list = sorted_dict(char_dict)
        for item in char_list:
            print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")

main()