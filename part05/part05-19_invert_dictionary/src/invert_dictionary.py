# Write your solution here
def invert(dictionary: dict):
  copy_dict = {}
  for key in dictionary:
    copy_dict[key] = dictionary[key]
  dictionary.clear()
  for key, value in copy_dict.items():
    dictionary[value] = key
  
if __name__ == "__main__":
  s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
  invert(s)
  print(s)