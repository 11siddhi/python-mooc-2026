# Write your solution here

total_items = int(input("How many items: "))
i = 1
item_list = []
while i <= total_items:
  item = int(input(f"Item {i}: "))
  item_list.append(item)
  i += 1

print(item_list)