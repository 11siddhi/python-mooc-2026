# Write your solution here
from datetime import datetime, timedelta
import csv

def final_points() -> dict:
  exam_duration = timedelta(hours=3)

  with open("start_times.csv", "r") as start_time:
    start_dict = {}
    for start_line in csv.reader(start_time, delimiter=";"):
      start_dict[start_line[0]] = start_line[1]  # {"name": "starting-time"}

  with open("submissions.csv", "r") as submissions:
    sub_dict = {}
    for sub_line in csv.reader(submissions, delimiter=";"):
      name = sub_line[0]
      time = sub_line[-1]
    
      start_time = datetime.strptime(start_dict[name], "%H:%M")
      end_time = start_time + exam_duration
      sub_time = datetime.strptime(time, "%H:%M")

      if sub_time > end_time:
        continue
      task = sub_line[1]
      points = int(sub_line[2])

      if name not in sub_dict:
        sub_dict[name] = {}

      if task not in sub_dict[name]:
        sub_dict[name][task] = points
        continue
      if points > sub_dict[name][task]:
        sub_dict[name][task] = points  # {"name": {"task": point}}
  
  total = 0
  final_points = {}
  for name, task_points in sub_dict.items():
    total = sum(task_points.values())
    final_points[name] = total

  return final_points


if __name__ == "__main__":
  final_points()