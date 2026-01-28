# Write your solution here
def length_of_longest(new_list):
    longest_len = 0
    for item in new_list:
        item_len = len(item)
        if item_len > longest_len:
            longest_len = item_len
    return longest_len

if __name__ == "__main__":
    print(length_of_longest(["first", "second", "fourth", "eleventh"]))
    print(length_of_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))