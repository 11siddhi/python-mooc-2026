# Write your solution here
def new_person(name: str, age: int) -> tuple:
  if name == "":
    raise ValueError(f"{name} is an empty string")
  if len(name) > 40:
    raise ValueError(f"{name} is longer than 40 characters")
  if len(name.split(" ")) < 2:
    raise ValueError(f"{name} contains less than two words")
  if age < 0:
    raise ValueError(f"{age} is a negative number")
  if age > 150:
    raise ValueError(f"{age} is greater than 150")
  return (name, age)