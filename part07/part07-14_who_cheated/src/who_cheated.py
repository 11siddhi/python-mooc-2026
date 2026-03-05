# Write your solution here
from datetime import datetime, timedelta

def cheaters():
  exam_duration = timedelta(hours=3)

  with open("start_times.csv", "r") as start_time:
    start_dict = {}
    for start_line in start_time:
      start_line = start_line.strip()
      parts_start = start_line.split(";")
      start_dict[parts_start[0]] = parts_start[1]  # {"name": "starting-time"}

  with open("submissions.csv", "r") as submissions:
    sub_dict = {}
    for sub_line in submissions:
      sub_line = sub_line.strip()
      parts_sub = sub_line.split(";")
      if not parts_sub[0] in sub_dict:
        sub_dict[parts_sub[0]] = []
      sub_dict[parts_sub[0]].append(parts_sub[1:]) # {"name": [task, point, submission-time]}

  cheaters = []
  for name in start_dict:
    start_time = datetime.strptime(start_dict[name], "%H:%M")
    end_time = start_time + exam_duration

    for values in sub_dict[name]:
      sub_time = datetime.strptime(values[2], "%H:%M")
      if sub_time > end_time:
        cheaters.append(name)
        break
  return cheaters

if __name__ == "__main__":
  cheaters()