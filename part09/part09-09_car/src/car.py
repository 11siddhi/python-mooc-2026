# WRITE YOUR SOLUTION HERE:
class Car:
  def __init__(self):
    self.__petrol_quantity = 0
    self.__odometer_reading = 0
  
  def fill_up(self):
    self.__petrol_quantity = 60

  def drive(self, km: int):
    if km > self.__petrol_quantity:
      km = self.__petrol_quantity
    self.__petrol_quantity -= km
    self.__odometer_reading += km
      
  def __str__(self):
    return f"Car: odometer reading {self.__odometer_reading} km, petrol remaining {self.__petrol_quantity} litres"

if __name__ == "__main__":
  car = Car()
  print(car)
  car.fill_up()
  print(car)
  car.drive(20)
  print(car)
  car.drive(50)
  print(car)
  car.drive(10)
  print(car)
  car.fill_up()
  car.fill_up()
  print(car)
      
