# Write your solution here
def distinct_numbers(num_list) -> list:
  distinct_list = []
  for num in num_list:
    if num not in distinct_list:
      distinct_list.append(num)
  sorted_list = sorted(distinct_list)
  return sorted_list
  
if __name__ == "__main__":
  distinct_numbers([3, 2, 2, 1, 3, 3, 1])
  distinct_numbers([3, 2, 2, 3, 3, 1])

