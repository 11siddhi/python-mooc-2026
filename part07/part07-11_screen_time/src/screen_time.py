# Write your solution here
from datetime import datetime, timedelta

def total_min_spent_today(strnum_list: list) -> int:
  total = 0
  for strnum in strnum_list:
    total += int(strnum)
  return total


filename = input("Filename: ")
start_dt = input("Starting date: ")
total_days = int(input("How many days: "))

start_dt = datetime.strptime(start_dt, "%d.%m.%Y")
next_day = timedelta(days=1)

print("Please type in screen time in minutes on each day (TV computer mobile):")

time_tracker = {}
total_min = 0
current_day = start_dt

for _ in range(total_days):
  scrn_time = input(f"Screen time {current_day.strftime('%d.%m.%Y')}: ")
  parts = scrn_time.split(" ")

  time_tracker[current_day.strftime("%d.%m.%Y")] = parts 
  total_min += total_min_spent_today(parts)

  current_day += next_day

last_dt = current_day - next_day # subtract the extra day added

with open(filename, "w") as my_file:
  my_file.write(f"Time period: {start_dt.strftime('%d.%m.%Y')}-{last_dt.strftime('%d.%m.%Y')}\n")
  my_file.write(f"Total minutes: {total_min}\n")
  my_file.write(f"Average minutes: {total_min/total_days:.1f}\n")

  for day, time_value in time_tracker.items():
    my_file.write(f"{day}: {time_value[0]}/{time_value[1]}/{time_value[2]}\n")

print(f"Data stored in file {filename}")


  
