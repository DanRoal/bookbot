def number_of_words(strin):
    splited = strin.split()
    return len(splited)

def character_apperances(text):
    characters = {}
    for char in text:
        char_lowercase = char.lower()
        if char_lowercase in characters:
            characters[char_lowercase] += 1
        else:
            characters[char_lowercase] = 1
    return characters

def sort_on(items):
    return items["num"]

def sorted_list_characters(dict_characters):
    list_characters = []
    
    for key in dict_characters:
        list_characters.append({"char": f"{key}", "num": dict_characters[key]})

    list_characters.sort(reverse=True, key=sort_on)

    return list_characters

