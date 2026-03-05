# Write your solution here
import json

def print_persons(filename: str):
  with open(filename, "r") as file:
    data = file.read()
  
  persons = json.loads(data)
  for person in persons:
    person_info = f'{person["name"]} {person["age"]} years ({", ".join(person["hobbies"])})'

    print(person_info)
        
if __name__ == "__main__":
  print_persons("file1.json")