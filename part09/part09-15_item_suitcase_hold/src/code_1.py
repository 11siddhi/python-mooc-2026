# Write your solution here:
# Items of different kinds with name and weight  
class Item:
  def __init__(self, name: str, weight: int):
    self.__name = name 
    self.__weight = weight 
  
  def name(self):
    return self.__name
  
  def weight(self):
    return self.__weight
  
  def __str__(self):
    return f"{self.__name} ({self.__weight} kg)"

# Pack items in suitcase    
class Suitcase:
  def __init__(self, max_weight: int):
    self.__max_weight = max_weight
    self.__items_list = []

  def weight(self, weight: int = 0):
    total = weight
    for item in self.__items_list:
      total += item.weight()
    return total

  def add_item(self, item: Item):
    if self.weight(item.weight()) <= self.__max_weight:
      self.__items_list.append(item)

  def __str__(self):
    if len(self.__items_list) == 1:
      return f"{len(self.__items_list)} item ({self.weight()} kg)"
    return f"{len(self.__items_list)} items ({self.weight()} kg)"

  def print_items(self):
    for item in self.__items_list:
      print(f"{item.name()} ({item.weight()} kg)")
  
  def heaviest_item(self):
    if self.__items_list:
      heavy_item = self.__items_list[0]
      for item in self.__items_list[1:]:
        if item.weight() > heavy_item.weight():
          heavy_item = item
      return heavy_item
    return None

# Pack suitcases in cargo 
class CargoHold:
  def __init__(self, max_weight: int):
    self.__max_weight = max_weight
    self.__suitcase_list = []
  
  def add_suitcase(self, suitcase: Suitcase):
    if suitcase.weight() <= self.__max_weight:
      self.__suitcase_list.append(suitcase)
      self.__max_weight -= suitcase.weight()
  
  def __str__(self):
    if len(self.__suitcase_list) == 1:
      return f"{len(self.__suitcase_list)} suitcase, space for {self.__max_weight} kg"
    return f"{len(self.__suitcase_list)} suitcases, space for {self.__max_weight} kg"
  
  def print_items(self):
    for suitcase in self.__suitcase_list:
      suitcase.print_items()


if __name__ == "__main__":
  book = Item("ABC Book", 2)
  phone = Item("Nokia 3210", 1)
  brick = Item("Brick", 4)

  adas_suitcase = Suitcase(10)
  adas_suitcase.add_item(book)
  adas_suitcase.add_item(phone)

  peters_suitcase = Suitcase(10)
  peters_suitcase.add_item(brick)

  cargo_hold = CargoHold(1000)
  cargo_hold.add_suitcase(adas_suitcase)
  cargo_hold.add_suitcase(peters_suitcase)

  print("The suitcases in the cargo hold contain the following items:")
  cargo_hold.print_items()