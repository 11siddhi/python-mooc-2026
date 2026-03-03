# write your solution here

def strlist2intlist(strlist: list):
  num = []
  for strnum in strlist:
    num.append(int(strnum))
  return num

# get student's information
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

# get exercises points
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

# get exam points and grade
def get_exam_grade(filename, total_exercises):
  with open(filename) as exam_points:
    grades = {}

    for points in exam_points:
      total = 0
      points = points.strip()
      parts = points.split(";")
      if parts[0] == "id":
        continue
      sid = int(parts[0])
      total += sum(strlist2intlist(parts[1:]))

      total += (total_exercises[sid]//4)
      if total >= 0 and total <= 14:
        grade = 0
      elif total >= 15 and total <= 17:
        grade = 1
      elif total >= 18 and total <= 20:
        grade = 2
      elif total >= 21 and total <= 23:
        grade = 3
      elif total >= 24 and total <= 27:
        grade = 4
      elif total >= 28:
        grade = 5
      else:
        grade = -1
      grades[sid] = [total, grade] 
  return grades 

def get_course_info(filename):
  course_info = {}
  with open(filename) as course_file:
    for line in course_file:
      line = line.strip()
      parts = line.split(":")
      parts[1] = parts[1].strip()
      if parts[1].isdecimal():
        parts[1] = int(parts[1])
      course_info[parts[0]] = parts[1]
  return course_info


def print_student_info(student_file, exercise_file, exam_file, course_info, txtfile, csvfile):
  students = get_student_name(student_file)
  exercises = get_total_exercise(exercise_file)
  grades = get_exam_grade(exam_file, exercises)
  course = get_course_info(course_info)
  

  with open(csvfile, "w") as resultcsv, open(txtfile, "w") as resulttxt:
    resulttxt.write(f"{course['name']}, {course['study credits']} credits\n")
    resulttxt.write("======================================\n")
    resulttxt.write(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
    
    for key, sname in students.items():
      name = f"{sname[0]} {sname[1]}"
      exec_nbr = exercises[key]
      exec_pts = exec_nbr//4
      tot_pts = grades[key][0]
      exm_pts = tot_pts - exec_pts
      gr = grades[key][1]

      resultcsv.write(f"{key};{name};{gr}\n")

      if key in exercises:
        resulttxt.write(f"{name:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{gr:<10}\n")
      else:
        resulttxt.write("No completed exercises.\n")




# if __name__ == "__main__":
std_file = input("Student information: ")
exer_file = input("Exercises completed: ")
exam_points = input("Exam points: ")
course_info = input("Course information: ")

# std_file = "students1.csv"    #input("Student information: ")
# exer_file = "exercises1.csv"     #input("Exercises completed: ")
# exam_points = "exam_points1.csv"   #input("Exam points: ")
# course_info = "course1.txt"
print_student_info(std_file, exer_file, exam_points, course_info, "results.txt", "results.csv")
