import sys

from stats import word_count, letters_in_book, sort_letters




def get_book_text(book_path):
    
    book = book_path
    with open(book, "r", encoding="utf-8-sig") as f:
        book = f.read()
        num_words = word_count(book)
        letter_count = letters_in_book(book)
        sorted = sort_letters(letter_count)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        
        for item in sorted:
            if item["char"].isalpha:
                print(f"{item["char"]}: {item["num"]}")
        
        print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return get_book_text(sys.argv[1])

if __name__ == "__main__":
    main()