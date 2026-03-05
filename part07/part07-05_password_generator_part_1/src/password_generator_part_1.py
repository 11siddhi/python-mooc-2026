# Write your solution here
from string import ascii_lowercase
from random import sample

def generate_password(length: int) -> str:
  lowercase_letters = ascii_lowercase 
  pwd = sample(lowercase_letters, length)
  pwd = "".join(pwd)
  return pwd

if __name__ == "__main__":
  for i in range(10):
      print(generate_password(8))