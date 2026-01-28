# Write your solution here
def no_shouting(str_list) -> list:
    calm_str_list = []
    for string in str_list:
        if not string.isupper():
            calm_str_list.append(string)
    return calm_str_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
