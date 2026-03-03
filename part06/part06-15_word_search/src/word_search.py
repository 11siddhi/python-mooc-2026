# Write your solution here
def read_file(filename) -> dict:
  valid_words = []
  with open(filename) as wordslist: 
    for word in wordslist:
      valid_words.append(word.strip())
  return valid_words

def check_for_dot(search_term: str, word: str) -> bool:
  for i, char in enumerate(search_term):
    if not char == '.':
      if not char == word[i]:
        return False
  return True

def check_for_asterisk(search_term: str, word: str) -> dict:
  no_wildcard = search_term.replace('*', "")
  if search_term[0] == '*':
    if word.endswith(no_wildcard):
      return True

  if search_term[-1] == '*':
    if word.startswith(no_wildcard):
      return True
  return False

def find_words(search_term: str) -> list:
  wordsdict = read_file("words.txt") 
  found_words = []
  for word in wordsdict:
    if '.' in search_term:
      if len(word) != len(search_term):
        continue
      if check_for_dot(search_term, word):
        found_words.append(word)

    elif '*' in search_term:
      if check_for_asterisk(search_term, word):
        found_words.append(word)   

    else:
      if search_term == word:
        found_words.append(word) 

  return found_words

# print(find_words(".a.e"))
# print(find_words("*vokes"))
