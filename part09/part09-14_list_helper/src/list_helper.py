# WRITE YOUR SOLUTION HERE:
class ListHelper:
  @classmethod
  def greatest_frequency(cls, my_list: list):
    frequencies = []
    most_common = my_list[0]

    for item in my_list[1:]:
      if item not in frequencies and my_list.count(item) > my_list.count(most_common):
        frequencies.append(item)
        most_common = item 

    return most_common
  
  @classmethod
  def doubles(cls, my_list: list):
    doubles = []

    for item in my_list:
      if item not in doubles and my_list.count(item) >= 2:
        doubles.append(item)

    return len(doubles)

if __name__ == "__main__":
  numbers = [1, 1, 2, 5]
  print(ListHelper.greatest_frequency(numbers))
  print(ListHelper.doubles(numbers))