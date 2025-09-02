import sys
from stats import count_words, count_character, sorting


def get_book_text (file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    char = count_character(text)
    final_list = sorting(char)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]}")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    for i in final_list:
        print (f"{i["char"]}: {i["num"]}")

main()

