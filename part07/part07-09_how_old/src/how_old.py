# Write your solution here
from datetime import datetime

new_millenium = datetime(1999, 12, 31)
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

if year < 2000:
  old = new_millenium - datetime(year, month, day)
  print(f"You were {old.days} days old on the eve of the new millennium.")
else:
  print("You weren't born yet on the eve of the new millennium.")
