def print_upper_words(words):
    """Function used to print each word that begins with an E or e, on a separate line with all letters in upper case"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words(words, must_start_with):
    """Function used to print each word that begins with a defined letter/letters, on a separate line with all letters in upper case"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
