# Write your solution here
def even_numbers(num_list: list) -> list:
  even_num = []
  for num in num_list:
    if num % 2 == 0:
      even_num.append(num)
  return even_num

if __name__ == "__main__":
  my_list = [1, 2, 3, 4, 5]
  new_list = even_numbers(my_list)
  print("original", my_list)
  print("new", new_list)