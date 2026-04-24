# Write your solution here:
def word_generator(characters: str, length: int, amount: int):
  if len(characters) < length * amount:
    while len(characters) < length * amount:
      characters += characters

  for i in range(amount):
    start_n = i * length
    end_n = length + start_n
    yield characters[start_n: end_n]
    

if __name__ == "__main__":
  wordgen = word_generator("abcdefg", 3, 5)
  for word in wordgen:
      print(word)