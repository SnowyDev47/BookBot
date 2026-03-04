# BOOKBOT STATISTICS FILE


def get_word_count(text):
    text_str = f"{text}"
    book_words = len(text_str.split())
    return book_words

def character_count(text):
    chars = {}
    text_str = f"{text}"
    lowercase_text = text_str.lower()   
    
    for char in lowercase_text:
        if char.isalpha():
            for ch in char:
                if ch in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    dict_list = []

    for char in dict:
        count = dict[char]
        new_dict = {"char": char, "num": count}
        dict_list.append(new_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

