from stats import count_words
from stats import count_characters
from stats import sorted_dict
import sys

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text(sys.argv[1])
    num_words = count_words(file_contents)
    word_dict = count_characters(file_contents)
    # WHY GOD WHY IN THE FUCK DOES ADDING THIS USELESS UNUSED VARIABLE CAUSE WORD_DICT TO PRINT TO THE CONSOLE SORTED????
    dict_list = sorted_dict(word_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in word_dict:
        i = list(i.values())
        if i[0].isalpha() == True:
            print(f"{i[0]}: {i[1]}")
    print("============= END ===============")

main()
