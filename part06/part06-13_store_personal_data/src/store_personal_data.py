# Write your solution here
def store_personal_data(person: tuple):
  # tuple: name: str, age: int, height: float 
  name, age, height = person[0], person[1], person[2]
  with open("people.csv", "a") as people:
    people.write(f"{name};{age};{height}\n")

p1 = ("Benoit Blanc", 55, 160.6)
store_personal_data(p1)

