# Write your solution here
pwd1 = input("Password: ")
pwd2 = input("Repeat password: ")

while pwd2 != pwd1:
    print("They do not match!")
    pwd2 = input("Repeat password: ")
    
print("User account created!")