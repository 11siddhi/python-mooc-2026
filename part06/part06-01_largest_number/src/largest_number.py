# write your solution here

def largest() -> int:
  largest_num = 0
  in_loop = False
  with open("numbers.txt") as numbers:
    for num in numbers:
      num = int(num)
      if not in_loop:
        largest_num = num
        in_loop = True
      if num > largest_num:
        largest_num = num
  return largest_num

# print(largest())
if __name__ == "__main__":
  largest()