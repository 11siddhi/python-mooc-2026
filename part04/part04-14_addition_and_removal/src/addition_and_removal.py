# Write your solution here
item_list = []
i = 1
while True:
  print(f"The list is now {item_list}")
  choice = input("a(d)d, (r)emove or e(x)it: ").lower()
  if choice == "r":
    item_list.pop()
    i -= 1
  elif choice == "d":
    item_list.append(i)
    i += 1
  elif choice == "x":
    print("Bye!")
    break
  