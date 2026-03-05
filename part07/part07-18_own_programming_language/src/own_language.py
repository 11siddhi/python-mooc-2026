# Write your solution here
from string import ascii_uppercase
import operator

def get_value(value: str, assigned_var_val: dict) -> int:
  val = int(value) if value.isdigit() else assigned_var_val[value] 
  return val

# set variable values to 0 in the beginning 
def set_var_val(assigned_var_val: dict):
  for char in ascii_uppercase:
    assigned_var_val[char] = 0

# assign variable value as per the command
def assign_var_val(cmd: str, var: str, val: str, assigned_var_val: dict):  
  val = get_value(val, assigned_var_val) 
  if cmd == "MOV":
    assigned_var_val[var] = val
  elif cmd == "ADD":
    assigned_var_val[var] += val 
  elif cmd == "SUB":
    assigned_var_val[var] -= val 
  elif cmd == "MUL":
    assigned_var_val[var] *= val

# set location's position 
def map_locations(program: list, locations: dict):
  for i, statement in enumerate(program):
    if statement.endswith(":"):
      statement = statement.replace(":", "")
      locations[statement] = i

# comparison for IF statements
def evaluate_condition(var1: str, var2: str, operation: str, assigned_var_val: dict) -> bool:
  var1 = get_value(var1, assigned_var_val)
  var2 = get_value(var2, assigned_var_val)
  comparison_operators = {
    "<": operator.lt,
    ">": operator.gt,
    "<=": operator.le,
    ">=": operator.ge,
    "==": operator.eq,
    "!=": operator.ne
  }
  return comparison_operators[operation](var1, var2)
  
      
# main program
def run(program: list) -> list:
  result = []
  assigned_var_val = {}
  set_var_val(assigned_var_val)
  i = 0
  locations = {}
  map_locations(program, locations)
  variable_keywrd = ["MOV", "ADD", "SUB", "MUL"]

  while i < len(program):
    statement = program[i]
    statement = statement.split()
    cmd = statement[0]

    if cmd == "IF":
      var1 = statement[1]
      var2 = statement[3]
      operation = statement[2]
      next_cmd = statement[4]
      next_cmd_val = statement[5]

      if evaluate_condition(var1, var2, operation, assigned_var_val):
        cmd = next_cmd
        statement = statement[4:]

    # handles assignment, addition, subtraction, multiplication
    if cmd in variable_keywrd:
      var = statement[1]
      val = statement[2]
      assign_var_val(cmd, var, val, assigned_var_val)
  
    # handles appending the print statement to list
    if cmd == "PRINT":
      val = statement[1]
      val = get_value(val, assigned_var_val)
      result.append(val)
    
    # jumps to the location specified
    if cmd == "JUMP":
      pos = statement[1]
      i = locations[pos] + 1
      continue

    if cmd == "END":
      return result
    
    i += 1
  return result
    

if __name__ == "__main__":

  # example 1:  
  program1 = []
  program1.append("MOV A 1")
  program1.append("MOV B 2")
  program1.append("PRINT A")
  program1.append("PRINT B")
  program1.append("MOV B A")
  program1.append("PRINT B")
  program1.append("END")
  result = run(program1)
  print(result)
  print("---------------------------")

  # example 2:
  program2 = []
  program2.append("MOV A 1")
  program2.append("MOV B 10")
  program2.append("begin:")
  program2.append("IF A >= B JUMP quit")
  program2.append("PRINT A")
  program2.append("PRINT B")
  program2.append("ADD A 1")
  program2.append("SUB B 1")
  program2.append("JUMP begin")
  program2.append("quit:")
  program2.append("PRINT A")
  program2.append("PRINT B")
  program2.append("PRINT 33")
  program2.append("PRINT 90")
  program2.append("END")
  result = run(program2)
  # map_locations(program2, locations)
  print(result)
  print("---------------------------")

  # example 3
  program3 = []
  program3.append("MOV A 1")
  program3.append("MOV B 1")
  program3.append("begin:")
  program3.append("PRINT A")
  program3.append("ADD B 1")
  program3.append("MUL A B")
  program3.append("IF B <= 10 JUMP begin")
  program3.append("END")
  result = run(program3)
  print(result)
  print("---------------------------")

  print(run(['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1', 'IF A <= N JUMP start']))