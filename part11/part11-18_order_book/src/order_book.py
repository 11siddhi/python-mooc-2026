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

