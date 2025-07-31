def sort_on(items):
    return items["num"]

def get_num_words(input_string: str):
    words = input_string.split()
    return len(words)

def character_frequency_count(input_string: str):
    character_counts = {}
    for character in input_string:
        lower_character = character.lower()
        if lower_character in character_counts:
            character_counts[lower_character] += 1
        else:
            character_counts[lower_character] = 1
    return character_counts

def sort_dictionary_to_list(dictionary:dict):
    new_list = []
    for entry_key in dictionary:
        if (entry_key.isalpha()):
            entry_value = dictionary[entry_key]
            new_list.append(
                {
                    'char': entry_key,
                    'num': entry_value
                }
            )
    new_list.sort(reverse=True, key=sort_on)
    return new_list
    