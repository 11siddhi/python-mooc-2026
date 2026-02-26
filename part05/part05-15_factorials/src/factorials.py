# Write your solution here
def factorials(n: int) -> dict:
  factorial = {}
  factorial[1] = 1
  for num in range(2, n+1):
    factorial[num] = factorial[num-1] * num
  return factorial

if __name__ == "__main__":
  k = factorials(5)
  print(k)
  print(k[1])
  print(k[3])
  print(k[5])
