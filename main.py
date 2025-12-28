from stats import number_of_words, character_apperances, sorted_list_characters
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    unsorted_characters = character_apperances(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(text)} total words") 
    print("--------- Character Count -------")
    for character in sorted_list_characters(unsorted_characters):
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    # print(sorted_list_characters(unsorted_characters))
    print("============= END ===============")

main()