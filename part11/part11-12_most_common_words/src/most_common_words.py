# WRITE YOUR SOLUTION HERE:
import string
def most_common_words(filename: str, lower_limit: int) -> dict:
  with open(filename, "r") as myfile:
    word_list = []
    for line in myfile:
      line = "".join([char for char in line if char not in string.punctuation]).strip().split()
      word_list += line

  return {word: word_list.count(word) for word in word_list if word_list.count(word) >= lower_limit}


if __name__ == "__main__":
  print(most_common_words("comprehensions.txt", 3))