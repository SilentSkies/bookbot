def word_count(book_text):
    book = book_text.split()
    return len(book)

def letters_in_book(book_text):
    words = book_text.split()
    letters = []
    letter_count = {}
    
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter not in letter_count:
                letter_count[letter] = 1
                continue
            letter_count[letter] += 1
            
    return letter_count
            
def sort_letters(letter_list: dict):
    def sort_on(items):
        return items["num"]
    
    characters_and_count=[]
    
    for k in letter_list:
        inner = {"char" : k, "num": letter_list[k]}
        characters_and_count.append(inner)
        
    
    characters_and_count.sort(reverse=True, key=sort_on)
    return characters_and_count
        
    
        
    
            