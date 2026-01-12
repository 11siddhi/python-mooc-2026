# Write your solution here
a = input("1st letter: ")
b = input("2nd letter: ")
c = input("3rd letter: ")

if (a > b and a < c) or (a < b and a > c):
    middle = a
elif (b > a and b < c) or (b < a and b > c):
    middle = b
else:
    middle = c

print("The letter in the middle is", middle)