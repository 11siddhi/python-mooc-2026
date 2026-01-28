# Write your solution here
def all_the_longest(my_list) -> list:
    long_item_list = []
    longest = 0

    for item in my_list:
        item_len = len(item)
        if item_len > longest:
            long_item_list.clear()
            long_item_list.append(item)
            longest = item_len
        elif item_len == longest:
            long_item_list.append(item)
    return long_item_list

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
