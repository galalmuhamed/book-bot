def report(words_count, charactrs_dicts):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document")
    print("")
    sort_dict = dict(sorted(charactrs_dicts.items(),
                            key=lambda item: item[-1], reverse=True))
    for key in sort_dict:
        print(f"The '{key}' character was found {sort_dict[key]} times")
    print("--- End report ---")


def character_count(str):
    obj = {}
    for character in str:
        lower_character = character.lower()
        if (lower_character.isalnum()):
            if (lower_character in obj):
                obj[lower_character] += 1
            else:
                obj.update({lower_character: 1})
    return obj


def words_count(str):
    str_arr = str.split()
    return len(str_arr)


def main():
    with open("books/frankenstein.txt") as f:
        readfile = f.read()
        words = words_count(readfile)
        character_dicts = character_count(readfile)
        report(words, character_dicts)


main()
