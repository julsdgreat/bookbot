import sys
from stats import get_book_text, get_num_words, count_character_occurrences, sort_character_counts


def print_report(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...\n")

    # Get book text
    text = get_book_text(book_path)

    # Get word count
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words\n")

    # Get character counts
    char_counts = count_character_occurrences(text)
    sorted_chars = sort_character_counts(char_counts)

    # Print character frequency report
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit the program with status code 1

    book_path = sys.argv[1]  # Get book path from command-line argument
    print_report(book_path)
