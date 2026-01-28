# Write your solution here
# You can test your function by calling it within the following block
def same_chars(word, ind1, ind2):
    word_len = len(word)
    if ind1 < word_len and ind2 < word_len:
        if word[ind1] == word[ind2]:
            return True
    return False

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))  # False
    print(same_chars("programmer", 6, 7)) # True
    print(same_chars("programmer", 0, 12)) # False
    print(same_chars("programmer", 0, 4)) # False