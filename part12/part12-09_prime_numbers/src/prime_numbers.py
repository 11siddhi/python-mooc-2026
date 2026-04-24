# Write your solution here
def prime_numbers():
  yield 2
  num = 2
  while True:
    is_prime = True
    num += 1
    for n in range(2, num):
      if num % n == 0:
        is_prime = False
        break 
    if is_prime:
      yield num
        
if __name__ == "__main__":
  numbers = prime_numbers()
  for i in range(8):
    # next(numbers)
    print(next(numbers))