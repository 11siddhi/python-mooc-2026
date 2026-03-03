# write your solution here

text = input("Write text: ")

valid_words = {}
with open("wordlist.txt") as wordslist: 
  for word in wordslist:
    valid_words[word.strip()] = True

result = []
txt_words = text.split()
for word in txt_words:
  if not word.lower() in valid_words:
    word = "*" + word + "*"
  result.append(word)

print(" ".join(result))
