def linear_word_search(string, word):
    #for element in string:
    #for x in range(0, len(string)):
    for x, element in enumerate(string):
        print(x, element)
        if string[x] == word:
            return x
    return None


def verify_word(index):
        if index is not None:
            print("Word found at index", index)
        else:
            print("Word not in list")

strings = ["happy", "birthday", "to", "you", "my", "friend"]

result = linear_word_search(strings, "birthday")
verify_word(result)