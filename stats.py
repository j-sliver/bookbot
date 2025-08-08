def get_num_words(text):
    split_text = text.split()
    num_words = len(split_text)
    return num_words

def get_char_count(text):
    lowered_text = text.lower()
    char_dict = {}
    for char in lowered_text:
        if char.isalpha() == True:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_dict(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list