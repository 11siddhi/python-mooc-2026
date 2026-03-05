# Write your solution here
from random import sample

def words(n: int, beginning: str) -> list:
  word_list = []
  found_list = []
  with open("words.txt") as words:
    for word in words:
      word_list.append(word.strip())
  
  for word in word_list:
    if word.startswith(beginning):
      found_list.append(word)
  return sample(found_list, n)

if __name__ == "__main__":
  word_list = words(3, "ca")
  for word in word_list:
      print(word)  