# Write your solution here:
class Clock:
  def __init__(self, hour, minute, seconds):
    self.seconds = seconds
    self.minutes = minute
    self.hour = hour
    
  def tick(self):
    self.seconds += 1

    if self.seconds == 60:
      self.seconds = 0
      self.minutes += 1

    if self.minutes == 60:
      self.minutes = 0
      self.hour += 1
    
    if self.hour == 24:
      self.hour = 0

  def set(self, hour: int, minute: int):
    self.hour = hour 
    self.minutes = minute 
    self.seconds = 0


  def __str__(self):
    return f"{self.hour:02}:{self.minutes:02}:{self.seconds:02}"


if __name__ == "__main__":
  clock = Clock(23, 59, 55)
  print(clock)
  clock.tick()
  print(clock)
  clock.tick()
  print(clock)
  clock.tick()
  print(clock)
  clock.tick()
  print(clock)
  clock.tick()
  print(clock)
  clock.tick()
  print(clock)

  clock.set(12, 5)
  print(clock)