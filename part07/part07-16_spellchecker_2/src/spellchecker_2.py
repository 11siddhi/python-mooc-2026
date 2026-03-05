# write your solution here
from difflib import get_close_matches

text = input("Write text: ")

valid_words = []
with open("wordlist.txt") as wordslist: 
  for word in wordslist:
    valid_words.append(word.strip())

result = []
invalid_words = []

txt_words = text.split()
for word in txt_words:
  if not word.lower() in valid_words:
    invalid_words.append(word)
    word = "*" + word + "*"
  result.append(word)

print(" ".join(result))

print("suggestions:")
for word in invalid_words:
  suggestions = get_close_matches(word, valid_words)
  print(f"{word}: {", ".join(suggestions)}")


