# write your solution here
def read_fruits() -> dict:
  fruits_dict = {}
  with open("fruits.csv") as fruits:
    for fruit in fruits:
      fruit = fruit.replace("\n", "")
      parts = fruit.split(";")
      fruits_dict[parts[0]] = float(parts[1])
  return fruits_dict