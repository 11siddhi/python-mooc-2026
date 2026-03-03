# Write your solution here
def check_problem(problem: str, result: str) -> bool:
  if '+' in problem:
    n1, n2 = problem.split("+")
    ans = int(n1) + int(n2) 
  elif '-' in problem:
    n1, n2 = problem.split("-")
    ans = int(n1) - int(n2) 
  return ans == int(result)

def write_in_file(filename: str, content: list):
  with open(filename, "w") as file:
    for line in content:
      file.write(line+'\n')

def filter_solutions():
  correct_sols = []
  incorrect_sols = []
  with open("solutions.csv", "r") as solutions:
    for line in solutions:
      line = line.strip()
      parts = line.split(";")
      if check_problem(parts[1], parts[2]):
        correct_sols.append(line)
      else:
        incorrect_sols.append(line)
  write_in_file("correct.csv", correct_sols)
  write_in_file("incorrect.csv", incorrect_sols)

if __name__ == "__main__":
  filter_solutions()
  
