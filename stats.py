def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def get_num_words(text):
    return len(text.split())

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    char_list = []
    for part in dictionary:
        char = {"char": part, "num": dictionary[part]}
        char_list.append(char)
    char_list.sort(reverse=True, key=sort_on)
    return char_list 

def print_report(filepath, num_words, chars_and_count):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = sort_dictionary(chars_and_count)
    for char_dict in sorted_chars:
        if char_dict['char'].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")


def get_char_count(text):
    chars_and_count = {}
    
    for char in text:
            if char.lower() in chars_and_count:
                chars_and_count[char.lower()] += 1
            else:
                chars_and_count[char.lower()] = 1

    return chars_and_count



    


