# Write your solution here
# just one dict -> add search term bag -> bag, garbage

def add2file(fin_word: str, en_word: str):
  with open("dictionary.txt", "a") as dictionary:
    dictionary.write(f"{fin_word};{en_word}\n")

def file2dict(filename: str) -> dict:
  words_dict = {}
  with open(filename) as dictionary:
    for line in dictionary:
      line = line.strip()
      if not line == "":
        parts = line.split(";")
        words_dict[parts[0]] = parts[1]              
  return words_dict
      
def add_word(dictionary: dict):
  fin_word = input("The word in Finnish: ").lower()
  en_word = input("The word in English: ").lower()
  dictionary[fin_word] = en_word
  add2file(fin_word, en_word)
  print("Dictionary entry added")

def search_word(dictionary: dict):
  word_found = False
  word = input("Search term: ").lower()
  for fin_word, en_word in dictionary.items():
    if word in fin_word or word in en_word:
      print(f"{fin_word} - {en_word}")
      word_found = True

  if not word_found:
    print(word, "word is not in dictionary. Please add it first.")

def dictionary():  
  words = file2dict("dictionary.txt")
  while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    cmd = input("Function: ")
    if cmd == "1":
      add_word(words)
    elif cmd == "2":
      search_word(words)
    elif cmd == "3":
      print("Bye!")
      break 
    else:
      print("Command not found!")
    
dictionary()