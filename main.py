import sys
from stats import count_words, count_characters, sort_chars


def get_book_text(path):
    with open(path) as f:
        book_contents = f.read()
    return book_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = (sys.argv)[1]
    text = get_book_text(path)
    num_words = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_chars(char_counts)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print (f"{char}: {count}")

    print ("============= END ===============")

if __name__ == "__main__":
    main()
