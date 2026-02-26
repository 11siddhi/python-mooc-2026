# Write your solution here
def times_ten(start_index: int, end_index: int) -> dict:
  times_ten = {}
  for num in range(start_index, end_index+1):
    times_ten[num] = num*10
  return times_ten

if __name__ == "__main__":
  d = times_ten(3, 6)
  print(d)
