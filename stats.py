def count_words(book_text):
    words = book_text.split()
    num_of_words = len(words)
    return num_of_words

def count_characters(book_text):
    letter_count = {}
    for i in book_text:
        lowercase_char = i.lower()
        if lowercase_char in letter_count:
            letter_count[lowercase_char] += 1
        else:
            letter_count[lowercase_char] = 1
    return (letter_count)

def sort_chars(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    def sort_on(dict):
        return dict["count"]

    chars_list.sort(reverse = True, key = sort_on)
    return chars_list
