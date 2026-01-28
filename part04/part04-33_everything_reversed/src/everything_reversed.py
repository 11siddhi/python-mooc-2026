# Write your solution here
def everything_reversed(str_list) -> list:
    reverse_list = str_list[::-1]
    everything_reverse_list = []
    for string in reverse_list:
        rev_str = string[::-1]
        everything_reverse_list.append(rev_str)
    return everything_reverse_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)