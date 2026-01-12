# Write your solution here
word = input("Please type in a word: ")
story = ""
last_word = ""
while word:
    if word == "end" or word == last_word:
        break
    story = story + word + " "
    last_word = word
    word = input("Please type in a word: ")

print(story)
