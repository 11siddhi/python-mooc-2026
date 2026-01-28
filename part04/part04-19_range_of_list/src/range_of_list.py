# Write your solution here
def range_of_list(list_name: list) -> int:
    largest_num = max(list_name)
    smallest_num = min(list_name)
    difference = largest_num - smallest_num
    return difference
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print(result)