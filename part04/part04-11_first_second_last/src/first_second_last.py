# Write your solution here
# You can test your function by calling it within the following block
def first_word(sentence):
    word = ""
    for char in sentence:
        if char == " ":
            break
        word += char
    return word

def second_word(sentence):
    words_found = 0
    word = ""
    for char in sentence:
        if char == " ":
            if words_found == 1:
                return word
            words_found += 1
        elif words_found == 1:
            word += char
    return word

def last_word(sentence):
    last_index = len(sentence) - 1
    last_word = ""
    while sentence[last_index] != " ":
        last_word += sentence[last_index]
        last_index -= 1
    return last_word[::-1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    print(second_word("first second"))
    print(first_word("hello"))