# Write your solution here
num1 = int(input("Number1: "))
num2 = int(input("Number2: "))
op = input("Operator: ")

if op == "add":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")