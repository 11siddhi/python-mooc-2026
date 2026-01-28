# Write your solution here
num_list = [1, 2, 3, 4, 5]

while True:
  index = int(input("Index: "))
  if index < 0:
    break 
  new_value = int(input("New value: "))
  num_list[index] = new_value
  print(num_list)
