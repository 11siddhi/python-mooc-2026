# write your solution here

def strlist2intlist(strlist: list):
  num = []
  for strnum in strlist:
    num.append(int(strnum))
  return num

def get_student_name(filename):
  with open(filename) as student_info:
    info = {}
    for student in student_info:
      student = student.strip()
      parts = student.split(";")
      if parts[0] == "id":
        continue
      sid = int(parts[0])
      name = parts[1:]
      info[sid] = name
  return info

def get_total_exercise(filename):
  with open(filename) as completed_exercises:
    total_exercises = {}
    for exercise in completed_exercises:
      exercise = exercise.strip()
      parts = exercise.split(";")
      if parts[0] == 'id':
        continue 
      sid = int(parts[0])
      total = sum(strlist2intlist(parts[1:]))
      total_exercises[sid] = total
  return total_exercises

def print_student_info(student_file, exercise_file):
  students = get_student_name(student_file)
  exercises = get_total_exercise(exercise_file)
  for key, sname in students.items():
    if key in exercises:
      print(f"{sname[0]} {sname[1]} {exercises[key]}")
    else:
      print("No completed exercises.")

# if __name__ == "__main__":
std_file = input("Student information: ")
exer_file = input("Exercises completed: ")
print_student_info(std_file, exer_file)
