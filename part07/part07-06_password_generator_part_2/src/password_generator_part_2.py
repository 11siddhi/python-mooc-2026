# Write your solution here
from string import ascii_lowercase, punctuation, digits
from random import sample, shuffle, choices

def generate_strong_password(length: int, add_numbers: bool, add_special_char: bool) -> str:

  # character groups  
  lowercase_letters = ascii_lowercase
  numbers = digits
  special_chars = '!?=+-()#' 

  pwd = []

  # Add atleast one lowercase letter  
  pwd += choices(lowercase_letters, k=1)

  # Add atleast one number if requested  
  if add_numbers:
    pwd += choices(numbers, k=1)

  # Add atleast one special character if requested 
  if add_special_char:
    pwd += choices(special_chars, k=1)

  # All character pools 
  allowed_chars = lowercase_letters
  if add_numbers:
    allowed_chars += numbers
  if add_special_char:
    allowed_chars += special_chars
  
  # Fill remaining length 
  remain_len = length - len(pwd)
  pwd += choices(allowed_chars, k=remain_len)

  # shuffle the list and convert it to string
  shuffle(pwd)
  pwd = "".join(pwd)

  return pwd

if __name__ == "__main__":
  print(generate_strong_password(2, False, False))
  print(generate_strong_password(8, False, False))
  print(generate_strong_password(8, True, True))
  print(generate_strong_password(8, True, False))
  for i in range(10):
    print(generate_strong_password(8, True, True))