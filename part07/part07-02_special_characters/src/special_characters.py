# Write your solution here
from string import ascii_letters, punctuation

def separate_characters(my_String: str) -> tuple:
  letters = ""
  punctuations = ""
  other = ""
  for char in my_String:
    if char in ascii_letters:
      letters += char 
    elif char in punctuation:
      punctuations += char
    else: 
      other += char 
  return (letters, punctuations, other)
if __name__ == "__main__":
  parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
  print(parts[0])
  print(parts[1])
  print(parts[2])