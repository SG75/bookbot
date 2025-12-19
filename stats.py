def count_words(text):
    words = text.split()
    return len(words)

def num_of_alphabets(text):
    counts = {}
    words = text.lower()
    for char in words:
        if char.isalpha():
            # char=char.lower()
            if char in counts:
                counts[char] += 1
            else:
                counts[char] =1
    return counts



def sort_on(d):
    return d["num"]

def sort_chars(chars):
    #convert dict -> list of dicts
    chars_list=[]

    for char,count in chars.items():
        chars_list.append({"char":char, "num": count})
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list




# def chars_dict_to_sorted_list(num_chars_dict):
#     sorted_list = []
#     for ch in num_chars_dict:
#         sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
#     sorted_list.sort(reverse=True, key=sort_on)
#     return sorted_list


if __name__ == "__main__":
    main()