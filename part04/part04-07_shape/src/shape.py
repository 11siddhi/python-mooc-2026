# Copy here code of line function from previous exercise and use it in your solution
def line(times, text):
    if text:
        print(text[0]*times)
    else:
        print("*"*times)

def shape(tri_size, tri_char, rect_height, rect_char):
    if rect_height != 0:
        rect_length = tri_size

    for i in range(tri_size):
        line(i+1, tri_char)
    
    for _ in range(rect_height):
        line(rect_length, rect_char)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
    print()
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")