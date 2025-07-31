from stats import get_num_words, character_frequency_count, sort_dictionary_to_list
import sys

def get_book_text(book_file: str):
    with open(book_file) as f:
        file_contents = f.read()
    return file_contents

def main (file_name: str):
    full_content = get_book_text(file_name)
    num_words = get_num_words(full_content)
    frequency_counts = character_frequency_count(full_content)
    frequency_count_list = sort_dictionary_to_list(frequency_counts)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_name}')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for entry in frequency_count_list:
        print(f"{entry['char']}: {entry['num']}")
    print('============= END ===============')

parameters = sys.argv
parameter_count = len(parameters)
if parameter_count != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    main(parameters[1])