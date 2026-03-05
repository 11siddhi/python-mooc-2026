# Write your solution here
from fractions import Fraction 

def fractionate(amount: int) -> list:
  fraction_list = []
  for i in range(amount):
    fraction_list.append(Fraction(1, amount))
  return fraction_list


if __name__ == "__main__":
  for p in fractionate(3):
      print(p)

  print()

  print(fractionate(5))
