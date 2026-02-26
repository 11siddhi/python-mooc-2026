# Write your solution here
def create_tuple(x: int, y: int, z: int) -> tuple:
  mylist = [x, y, z]
  return (min(mylist), max(mylist), sum(mylist))
