# Write your solution here

original_list = []
sorted_list = []

while True:
  item = int(input("New item: "))
  if item == 0:
    break
  original_list.append(item)
  sorted_list = sorted(original_list)
  print(f"The list now: {original_list}")
  print(f"The list in order: {sorted_list}")
print("Bye!")