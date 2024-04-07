

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    
    data = dict_of_all_chars_to_lower_case(text)
    sorted_list = characters_dict_to_sorted_list(data)
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(text)} words found in the document \n\n")
    report_book_stats(sorted_list)

def sort_on(dict):
    return dict["count"]

def get_book_text(path:str) -> str:
    with open("books/frankenstein.txt") as book:
        return book.read()


def count_words(text:str) -> int:
    words = text.split()
    return len(words)

def dict_of_all_chars_to_lower_case(text:str) -> dict:
    lower_text = text.lower()
    count = {}
    for char in lower_text:
        if char not in count:
            count[char] = 1
        else:
            count[char] +=1
    return count

def characters_dict_to_sorted_list(character_count:dict) -> list:
    '''
    ### Data in
    dictionary where character is the key and count is the value
    --> {character:count}
    ### Data out
    list of dictionaries where "letter" is key and char is value, and "count" is key and count is value. 
    --> ({"letter":character, "count": count})
    ### Sorted by frequency, most to least.
    '''

    new_list = []
    for key in character_count:
        if key.isalpha():
            new_list.append({"letter": key, "count":character_count[key]})
    new_list.sort(reverse=True, key=sort_on)       
    return new_list

def report_book_stats(character_list:list) -> str:
    for i in range(0, len(character_list)):
        print(f"The '{character_list[i]["letter"]}' was found {character_list[i]["count"]} times")
    print("--- End Report ---")





main()
