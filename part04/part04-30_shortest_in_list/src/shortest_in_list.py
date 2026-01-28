# Write your solution here
def shortest(new_list) -> str:
    shortest = ""
    for item in new_list:
        if shortest == "" or len(item) < len(shortest):
            shortest = item
    return shortest
if __name__ == "__main__":
    print(shortest(["first", "second", "fourth", "eleventh"]))
    print(shortest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))