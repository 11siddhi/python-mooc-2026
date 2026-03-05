# Write your solution here
from random import sample
def lottery_numbers(amount: int, lower: int, upper: int) -> list:
  number_pool = list(range(lower, upper+1))
  lottery_numbers = sample(number_pool, amount)
  lottery_numbers.sort()
  return lottery_numbers

if __name__ == "__main__":
  lottery_numbers(7, 1, 40)
