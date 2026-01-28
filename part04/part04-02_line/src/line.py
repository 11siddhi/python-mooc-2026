# Write your solution here
# You can test your function by calling it within the following block
def line(times, text):
    if text:
        print(text[0]*times)
    else:
        print("*"*times)

if __name__ == "__main__":
    line(5, "x")
    line(10, "LOL")
    line(3, "")