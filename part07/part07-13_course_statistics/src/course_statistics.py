# Write your solution here
import urllib.request
import json

def retrieve_all() -> list:
  url_data = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
  data = url_data.read()

  course_list = []
  json_data = json.loads(data)
  for course in json_data:
    if course["enabled"]:
      course_list.append((course["fullName"], course["name"], course["year"], sum(course["exercises"])))

  return course_list

def retrieve_course(course_name: str) -> dict:
  url_data = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
  data = url_data.read()

  course_data = json.loads(data)

  total_students = []
  total_hours = 0
  total_exer = 0

  for i in range(len(course_data)):
    if '0' not in course_data:
      week = str(i+1)
    else:
      week = str(i)

    total_students.append(course_data[week]["students"])
    total_hours += course_data[week]["hour_total"]
    total_exer += course_data[week]["exercise_total"]

  total_students = max(total_students)
  course_details = {
    'weeks': len(course_data),
    'students': total_students,
    'hours': total_hours,
    'hours_average': total_hours//total_students,
    'exercises': total_exer,
    'exercises_average': total_exer//total_students
  }

  return course_details


if __name__ == "__main__":
  retrieve_all() 
  print(retrieve_course("CCFUN"))
