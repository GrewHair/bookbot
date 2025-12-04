import sys
from stats import get_num_words
from stats import get_char_counts
from stats import get_sorted_char_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    char_counts = get_char_counts(book)
    sorted_char_counts = get_sorted_char_counts(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(char_counts)
    #print(sorted_char_counts)
    for item in sorted_char_counts:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

main()
