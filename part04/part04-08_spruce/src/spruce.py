# Write your solution here
# You can test your function by calling it within the following block

def spruce(height):
    print("a spruce!")

    # Print the triangular part of the spruce
    for row in range(height):
        spaces = height - row - 1
        stars = 2 * row + 1
        print(" " * spaces + "*" * stars)

    # Print the trunk of the spruce
    print(" " * (height - 1) + "*")



if __name__ == "__main__":
    spruce(5)