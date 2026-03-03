# Write your solution here

def add_entry(filename: str):
  content = input("Dairy entry: ")
  with open(filename, "a") as diary:
    diary.write(f"{content}\n")
  print("Diary saved")
  print()

def read_entry(filename: str):
  print("Entries:")
  with open(filename) as diary:
    for line in diary:
      line = line.strip()
      print(line)

def main():
  file = "diary.txt"
  while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    cmd = int(input("Function: "))
    if cmd == 1:
      add_entry(file)
    elif cmd == 2:
      read_entry(file)
    elif cmd == 0:
      print("Bye now!")
      break

main()