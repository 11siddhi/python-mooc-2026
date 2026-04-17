# WRITE YOUR SOLUTION HERE:
class SimpleDate:
  def __init__(self, day: int, mon: int, year: int):
    self.day = day
    self.mon = mon 
    self.year = year 
  
  def __str__(self):
    return f"{self.day}.{self.mon}.{self.year}"
  
  def __repr__(self):
    return f"{self.year:02}.{self.mon:02}.{self.day}"

  def __lt__(self, another):
    return repr(self) < repr(another)

  def __gt__(self, another):
    return repr(self) > repr(another)
  
  def __eq__(self, another):
    return repr(self) == repr(another)
  
  def __ne__(self, another):
    return repr(self) != repr(another)
  
  def __add__(self, days: int):
    dmon = 30
    dyear = 360
    myear = 12
    new_day = SimpleDate(self.day, self.mon, self.year)
    new_day.day += days 
    while new_day.day > dmon:
      new_day.day -= dmon 
      new_day.mon += 1
    while new_day.mon > myear:
      new_day.mon -= myear
      new_day.year += 1

    return new_day

  def __sub__(self, another: "SimpleDate"):
    dmon = 30
    dyear = 360
    self_days = self.year * dyear + self.mon * dmon + self.day 
    another_days = another.year * dyear + another.mon * dmon + another.day 
    return abs(self_days - another_days)

if __name__ == "__main__":
  sd1 = SimpleDate(9, 9, 1976)
  sd2 = SimpleDate(9, 10, 1976)

  print(sd1 < sd2)
