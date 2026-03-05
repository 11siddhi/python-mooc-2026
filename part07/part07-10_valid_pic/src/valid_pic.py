# Write your solution here
from datetime import date

def valid_control_char(bday, pid, control) -> bool:
  char_string = '0123456789ABCDEFHJKLMNPRSTUVWXY'
  num = int(bday + pid)
  index = num % 31
  z = char_string[index]
  return z == control

def is_it_valid(pic: str) -> bool:
  marker = {"+": 1800, "-": 1900, "A": 2000}
  if len(pic) != 11:
    return False

  century = pic[6]
  if century not in marker:
    return False

  bday = pic[:6]
  month = int(bday[2:4])
  day = int(bday[:2])  
  year = int(bday[4:])
  year += marker[century]
  try:
    date(year, month, day)
  except ValueError:
    return False
  
  identifier = pic[7:10]
  if len(identifier) != 3 or not identifier.isdecimal():
    return False

  control_char = pic[-1]
  return valid_control_char(bday, identifier, control_char)
  

if __name__ == "__main__":
  print(is_it_valid('230594+246L'))
  print(is_it_valid('230827-906F'))
  print(is_it_valid('310823A9877'))
  print(is_it_valid('081842-720N'))