# Write your solution here

# Part 1
def add_student(students: dict, name: str):
  students[name] = []

def print_student(students: dict, name: str):
  if name in students:
    print(f"{name}:")

    # if student has completed courses
    if students[name]:
      total_course = len(students[name])
      print(f" {total_course} completed courses:")

      # Loop through all courses and calculate total score
      total_score = 0
      for i, com_course in enumerate(students[name]):
        total_score += com_course[1]
        print(f"  {com_course[0]} {com_course[1]}")

      print(f" average grade {total_score/total_course}")
    
    else:
      print(" no completed courses")

  else:
    print(f"{name}: no such person in the database")

def add_course(students: dict, name: str, course: tuple):
  # add course if student exist and grade is not 0
  if name in students and course[1] != 0:

    # if student already has courses 
    if students[name]:

      # Check if course already exists
      for i, com_course in enumerate(students[name]):
        if course[0] == com_course[0]:
          if course[1] > com_course[1]:
            students[name][i] = course  # Replace only if new grade is better
          return
  
    students[name].append(course)

def summary(students: dict):
  total_std = len(students)

  max_courses = 0           # Highest number of completed courses
  max_grade = 0             # Highest average grade

  max_course_std = ""       # Student with most completed courses
  max_grade_std = ""        # Student with best average grade

  for std_name, courses in students.items():
    total_course = len(courses)

    # track student with most courses
    if total_course > max_courses:
      max_courses = total_course
      max_course_std = std_name

    total_grade = 0

    # sum grades for average calculation
    for course in courses:
      total_grade += course[1]
    
    if total_course != 0:
      avg_grade = total_grade/total_course

    # track student with best average grade
    if avg_grade > max_grade:
      max_grade = avg_grade
      max_grade_std = std_name
  
  print(f"students {total_std}")
  print("most courses completed", max_courses, max_course_std) 
  print("best average grade", max_grade, max_grade_std) 


if __name__ == "__main__":
  students = {}
  # add_student(students, "Peter")
  # add_student(students, "Eliza")
  # add_course(students, "Peter", ("Data Structures and Algorithms", 1))
  # add_course(students, "Peter", ("Introduction to Programming", 1))
  # add_course(students, "Peter", ("Advanced Course in Programming", 1))
  # add_course(students, "Eliza", ("Introduction to Programming", 5))
  # add_course(students, "Eliza", ("Introduction to Computer Science", 4))
  # print_student(students, "Peter")
  # print_student(students, "Eliza")
  # summary(students)


  add_student(students, "Peter")
  add_course(students, "Peter", ("Software Development Methods", 1))
  add_course(students, "Peter", ("Software Development Methods", 5))
  print_student(students, "Peter")
