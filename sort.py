def sort_list(words, remove_duplicates=False, to_uppercase=False):
    if remove_duplicates:
        words = list(set(words))
    if to_uppercase:
        words = [word.upper() for word in words]
    words.sort()
    return words