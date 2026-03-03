# Write your solution here
def read_input(statement: str, n1: int, n2: int):
  while True:
    try:
      num = int(input(statement))
      if num < n1 or num > n2:
        print(f"You must type in an integer between {n1} and {n2}")
        continue
      return num 
    except:
      print(f"You must type in an integer between {n1} and {n2}")
      continue
  
if __name__ == "__main__":
  number = read_input("Please type in a number: ", 5, 10)
  print("You typed in:", number)