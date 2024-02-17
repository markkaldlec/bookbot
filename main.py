file_path = "./books/frankenstein.txt"

def main():
    with open(file_path) as file:
        file_contents = file.read()

    print(file_contents)
    word_count = count_words(file_contents)
    letters = letter_count(file_contents)
    list_of_dic = sort_letters(letters)
    print(f'File contains {word_count} words. \n')
    print_list_of_dict(list_of_dic)
 


def count_words(str):
    words_list = str.split()
    word_count = len(words_list)
    return word_count
    

def letter_count(str):
    str_in_lower = str.lower()
    letters = {}
    words_list = str_in_lower.split()
    for word in words_list:
        for letter in word:
            if letter.isalpha() == False:
                continue
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def sort_on(dict):
    return dict["count"]

def sort_letters(dic):
    list_of_dict = []
    for entry in dic:
        list_of_dict.append({"character": entry, "count": dic[entry] })
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def print_list_of_dict(list):
    for dict in list:
        print(f'Letter: {dict['character']} was found {dict['count']} times.')

main()
