# Write your solution here
# If you use the classes made in the previous exercise, copy them here
# Write your solution here:
class Task:
  _id_counter = 0  # class variable

  def __init__(self, description, programmer, hours):
    Task._id_counter += 1
    self.id = Task._id_counter
    self.description = description
    self.programmer = programmer
    self.workload = hours
    self.completion = False
    
  def is_finished(self):
    return self.completion

  def mark_finished(self):
    self.completion = True
  
  def __str__(self):
    return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'NOT FINISHED' if self.completion == False else 'FINISHED'}"


class OrderBook:
  def __init__(self):
    self.tasks = []

  def add_order(self, description, programmer, workload):
    self.tasks.append(Task(description, programmer, workload))

  def all_orders(self):
    return self.tasks
  
  def programmers(self):
    return list(set([task.programmer for task in self.tasks]))
  
  def mark_finished(self, id: int):
    for task in self.tasks:
      if task.id == id:
        task.mark_finished()
        return
    raise ValueError("Invalid id number")
  
  def finished_orders(self):
    return [task for task in self.tasks if task.completion]
  
  def unfinished_orders(self):
    return [task for task in self.tasks if not task.completion]
    
  def status_of_programmer(self, programmer: str):
    (ftask, utask, fworkload, uworkload) = (0, 0, 0, 0)
    if programmer not in self.programmers():
      raise ValueError("Invalid programmer name")    

    for task in self.tasks:
      if task.programmer == programmer:
        if task.is_finished():
          ftask += 1
          fworkload += task.workload
        else:
          utask += 1
          uworkload += task.workload
      
    return (ftask, utask, fworkload, uworkload)

class OrderBookApplication:
  def __init__(self):
    self.__orderbook = OrderBook()
    
  def help(self):
    print("commands:")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")

  def add_order(self):
    desc = input("description: ")
    try: 
      programmer, workload = input("programmer and workload estimate: "). split()
    except ValueError:
      print("erroneous input")
      return
    if workload.isdigit():
      self.__orderbook.add_order(desc, programmer, int(workload))
      print("added!")
    else:
      print("erroneous input")

  def finished_tasks(self):
    tasks = self.__orderbook.finished_orders()
    if not tasks:
      print("no finished tasks")
    for task in tasks:
      print(task)
    
  def unfinished_tasks(self):
    tasks = self.__orderbook.unfinished_orders()
    if not tasks:
      return "no unfinished tasks"
    for task in tasks:
      print(task)

  def mark_finished(self):
    try:
      id_num = int(input("id: "))
      self.__orderbook.mark_finished(id_num)
    except ValueError:
      print("erroneous input")
      return
    print("marked as finished")
  
  def programmers(self):
    programmers = self.__orderbook.programmers()
    for programmer in programmers:
      print(programmer)
    
  def status_of_programmer(self):
    programmer = input("programmer: ")
    try:
      ftask, utask, fworkload, uworkload = self.__orderbook.status_of_programmer(programmer)
    except ValueError:
      print("erroneous input")
      return
    print(f"tasks: finished {ftask} not finished {utask}, hours: done {fworkload} scheduled {uworkload}")

  def execute(self):
    self.help()
    while True:
      print("")
      cmd = input("command: ")
      if cmd == "0":
        break
      elif cmd == "1":
        self.add_order()
      elif cmd == "2":
        self.finished_tasks()
      elif cmd == "3":
        self.unfinished_tasks() 
      elif cmd == "4":
        self.mark_finished()
      elif cmd == "5":
        self.programmers() 
      elif cmd == "6":
        self.status_of_programmer() 
      else:
        self.help()

orders = OrderBookApplication()
orders.execute()