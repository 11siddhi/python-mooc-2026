# tee ratkaisusi tänne
class Course:
  def __init__(self):
    self.__name = ""
    self.__grade = 0
    self.__credit = 0
  
  def add_course(self, name: str, grade: int, credit: int):
    self.__name = name
    if grade > self.__grade:
      self.__grade = grade 
    self.__credit = credit
  
  def name(self):
    return self.__name 
  
  def grade(self):
    return self.__grade
  
  def credit(self):
    return self.__credit 

class CourseRecords:
  def __init__(self):
    self.__records = {}
  
  def add_course(self, name: str, grade: int, credit: int):
    if name not in self.__records:
      self.__records[name] = Course()
    self.__records[name].add_course(name, grade, credit)
  
  def get_course_data(self, name):
    if name not in self.__records:
      return None
    return self.__records[name]
  
  def statistics(self):
    total_credit = 0
    total_grade = 0
    grade_dict = {}
    for course in self.__records.values():
      total_credit += course.credit()
      total_grade += course.grade()

      grade = course.grade()
      if grade not in grade_dict:
        grade_dict[grade] = 0
      grade_dict[grade] += 1

    print(f"{len(self.__records)} completed courses, a total of {total_credit} credits")
    if self.__records:
      print(f"mean {total_grade/len(self.__records):.1f}")
    else:
      print(f"mean 0.0")
    print("grade distribution")
    
    grade = 5
    while grade > 0:
      if grade in grade_dict:
        print(f"{grade}:",  'x'*grade_dict[grade])
      else:
        print(f"{grade}: ")
      grade -= 1

      
class CourseRecordsApplication:
  def __init__(self):
    self.__course_records = CourseRecords()

  def help(self):
    print("1 add course")
    print("2 get course data")
    print("3 statistics")
    print("0 exit")
  
  def add_course(self):
    course_name = input("course: ")
    course_grade = int(input("grade: "))
    course_credit = int(input("credit: "))
    self.__course_records.add_course(course_name, course_grade, course_credit)

  def get_course_data(self):
    course_name = input("course: ")
    data = self.__course_records.get_course_data(course_name)
    if data is None:
      print("no entry for this course")
      return
    print(f"{data.name()} ({data.credit()} cr) grade {data.grade()}")
    return
  
  def statistics(self):
    self.__course_records.statistics()

  def execute(self):
    self.help()
    while True:
        print("")
        command = input("command: ")
        if command == "0":
            break
        elif command == "1":
            self.add_course()
        elif command == "2":
            self.get_course_data()
        elif command == "3":
            self.statistics()
        else:
            self.help()
          
courses = CourseRecordsApplication()
courses.execute()
