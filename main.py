import sys
from stats import count_words, num_of_alphabets,sort_chars

if (len(sys.argv) < 2):
    print (f" Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents


def main():
    # text = get_book_text("./books/frankenstein.txt")
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    stats = num_of_alphabets(text)
    sorted_chars = sort_chars(stats)

    print (f"============ BOOKBOT ============")
    print (f"Analyzing book found at books/frankenstein.txt...")
    print (f"----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    print("f============= END ===============")
    

if __name__ == "__main__":
    main()

  