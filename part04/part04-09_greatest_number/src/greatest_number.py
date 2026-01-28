# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n3 and n2 >= n1:
        return n2
    else:
        return n3

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
    print(greatest_number(3, 4, 1)) # 4
    print(greatest_number(99, -4, 7)) # 99
    print(greatest_number(0, 0, 0)) # 0
    print(greatest_number(1, 1, -1)) # 1