"""
Bookbot - A command-line text analysis tool.
Usage CLI: python3 main.py <path_to_book
"""
import sys
from stats import (
    get_book_text, 
    get_num_words, 
    get_char_count, 
    sort_dictionary,
    print_report
)
#Main Function - handles CLI args and runs analysis
def main():
    try:
        if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            filepath = sys.argv[1]
            text = get_book_text(filepath)
            num_words = get_num_words(text)
            chars_and_count = get_char_count(text)
            print_report(filepath, num_words, chars_and_count)
    except Exception as e:
      print(f"Error encountered: {e}")
     
if __name__ == "__main__":
    main()