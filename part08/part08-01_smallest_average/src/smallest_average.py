# Write your solution here
def calculate_average(person: dict) -> float:
  total_results = 3
  person_total = person["result1"] + person["result2"] + person["result3"]
  return person_total/total_results

def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
  smallest_avg = person1
 
  if calculate_average(person2) < calculate_average(smallest_avg):
      smallest_avg = person2

  if calculate_average(person3) < calculate_average(smallest_avg):
      smallest_avg = person3

  return smallest_avg
    

if __name__ == "__main__":
  person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
  person3 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
  person2 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

  print(smallest_average(person1, person2, person3))

  print(smallest_average({"result1": 9,"result2": 9,"result3": 9}, {"result1": 7,"result2": 7,"result3": 7}, {"result1": 8,"result2": 8,"result3": 8}))
