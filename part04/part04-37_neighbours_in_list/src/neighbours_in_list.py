# Write your solution here
def longest_series_of_neighbours(num_list) -> int:
    prev_num = 0
    prev_len = 0
    length = 0
    for num in num_list:
        if num == prev_num + 1 or num == prev_num - 1:
            prev_num = num
            length += 1
        else:
            if length > prev_len:
                prev_len = length
            length = 1
            prev_num = num
        if length > prev_len:
                prev_len = length
    return prev_len

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0] 
    print(longest_series_of_neighbours(my_list))

    my_list = [1, 2, 5, 4, 3, 4]
    print(longest_series_of_neighbours(my_list))

    my_list = [0, 2, 4, 5, 6, 7, 10, 11, 12, 100, 101]
    print(longest_series_of_neighbours(my_list))

    