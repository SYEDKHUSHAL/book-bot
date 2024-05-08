def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    dict_list = get_sorted_list_of_dict(chars_dict)
    print_report(dict_list, num_words)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return (len(words))

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars.keys():
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]
  
def get_sorted_list_of_dict(chars_dict):
    dict_list = []
    for x in chars_dict:
        if(x.isalpha()):
            dict_list.append({"char": x, "num": chars_dict[x]})
            
    dict_list.sort(reverse = True, key = sort_on)
    return dict_list
    
def print_report(dict_list, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for x in dict_list:
        print(f"The {x["char"]} character was found {x["num"]} times")
    print("--- End report ---")
    

main()