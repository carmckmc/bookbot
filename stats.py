def count_words(file_contents):
    return len(file_contents.split())
    
def count_characters(file_contents):
    file_contents = file_contents.lower()
    character_count = {}
    for character in file_contents:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    char_count = [{"char": k, "num": v} for k, v in character_count.items()]
    return char_count

def sorted_dict(char_count):
    def sort_on(items):
        return items["num"]

    return char_count.sort(reverse=True, key=sort_on)
