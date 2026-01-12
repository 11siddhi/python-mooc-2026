# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
total_num = 0
addition = 0
negative = 0
positive = 0
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    total_num += 1
    addition += num
    if num < 0:
        negative += 1
    else: 
        positive += 1

print("Numbers typed in", total_num)
print("The sum of the numbers is", addition)
print("The mean of the numbers is", (addition/total_num))
print("Positive numbers", positive)
print("Negative numbers", negative)