# Write your solution here
def formatted(float_list: list) -> list:
    formatted_list = []
    for number in float_list:
        formatted_num = f"{number:.2f}"
        formatted_list.append(formatted_num)
    return formatted_list

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)