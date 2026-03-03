# Write your solution here
def filter_incorrect():
  with open("lottery_numbers.csv") as lottery_numbers, open("correct_numbers.csv", "w") as correct_numbers:
    for line in lottery_numbers:
      line = line.strip()
      parts = line.split(";")

      # Validate week format (must be "week X")
      week = parts[0].split(" ")
      if not week[1].isdecimal():
        continue

      numbers = parts[1].split(",")

      # Validate that there are exactly 7 numbers
      if len(numbers) != 7:
          continue

      isnum_valid = True
      # Validate each number: numeric, in range, no duplicates
      for num in numbers:
        if not num.isdecimal():
          isnum_valid = False
          break
        num = int(num)
        if num < 1 or num > 40 or numbers.count(str(num)) > 1:
          isnum_valid = False
          break
        
      if isnum_valid:
        correct_numbers.write(line + "\n")
      


if __name__ == "__main__":  
  filter_incorrect()