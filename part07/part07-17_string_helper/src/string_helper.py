# Write your solution here
from string import ascii_letters

def change_case(orig_string: str):
  new_str = ""
  for char in orig_string:
    if char.islower():
      new_str += char.upper()
    elif char.isupper():
      new_str += char.lower()
    else:
      new_str += char
  return new_str

def split_in_half(orig_string: str):
  half = len(orig_string) // 2
  return (orig_string[:half], orig_string[half:])

def remove_special_characters(orig_string: str):
  new_str = ""
  for char in orig_string:
    if char in ascii_letters or char in '0123456789' or char == " ":
      new_str += char      
  return new_str

if __name__ == "__main__":
  my_string = "Well hello there!"

  print(change_case(my_string))

  p1, p2 = split_in_half(my_string)

  print(p1)
  print(p2)

  m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
  print(m2)