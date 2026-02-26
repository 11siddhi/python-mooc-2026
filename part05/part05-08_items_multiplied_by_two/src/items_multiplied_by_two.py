# Write your solution here
def double_items(numbers: list) -> list:
  new_num_list = []
  for num in numbers:
    new_num_list.append(num*2)
  return new_num_list


if __name__ == "__main__":
  numbers = [2, 4, 5, 3, 11, -4]
  numbers_doubled = double_items(numbers)
  print("original:", numbers)
  print("doubled:", numbers_doubled)