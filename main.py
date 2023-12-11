def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    count_letters= get_char_frequency(text)
    print(count_letters)
    for char, count in sorted(count_letters.items()):
        print(f"The '{char}' charater was found {count} times")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_frequency(text):
    # Convert text to lowercase and remove non-alphabetic characters
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())

    # Count the frequency of each character
    char_frequency = {}
    for char in cleaned_text:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    return char_frequency

main()