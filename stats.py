def get_num_words(text):
    words = text.split()
    return len(words)


def count_character_occurrences(text):
    char_counts = {}
    for char in text.lower():  # Convert to lowercase to avoid duplicates
        char_counts[char] = char_counts.get(char, 0) + 1  # Update count

    return char_counts


def sort_character_counts(char_counts):
    """Sorts character occurrences from highest to lowest and filters only letters."""
    sorted_list = sorted(
        [{"char": char, "count": count}
            for char, count in char_counts.items() if char.isalpha()],
        key=lambda item: item["count"],
        reverse=True
    )
    return sorted_list  # ✅ Make sure this line exists!


def get_book_text(filepath):
    """Reads a book file and returns its content as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

    return sorted_list
