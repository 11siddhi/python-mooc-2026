# Write your solution here

def search(phone_book: dict, name: str) -> str:
  if name in phone_book:
    return phone_book[name]
  else:
    return "no number"

def add(phone_book: dict, name: str, num: str):
  phone_book[name] = num

phone_book = {}
while True: 
  command = int(input("command (1 search, 2 add, 3 quit): "))
  if command == 1:
    name = input("name: ")
    print(search(phone_book, name))

  elif command == 2:
    name = input("name: ")
    number = input("number: ")
    add(phone_book, name, number)
    print("ok!")

  elif command == 3:
    print("quitting...")
    break
  else: 
    print("No such command")
    break