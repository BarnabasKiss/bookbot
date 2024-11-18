def main():
    book_path = "books/frankenstein.txt"
    book_text = get_booktext(book_path)
    word_count = count_words(book_text)
    character_dict = count_characters(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(character_dict)
    
    print(f"--- Beginn report of {book_path} ---")
    print()
    print(f"{word_count} words found in the document")
    print()

    for item in chars_sorted_list:
        print(f"The {item["char"]} character was found {item["num"]} times.")

    print("---End report ---")



def count_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

def get_booktext(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    chars = {}
    for char in text.lower():
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars








main()