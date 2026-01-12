# Write your solution here
points = int(input("How many points [0-100]: "))
grade = ""
if points < 0 or points > 100:
    grade = "impossible!"
elif points <= 49:
    grade = "fail"
elif points <= 59:
    grade = "1"
elif points <= 69:
    grade = "2"
elif points <= 79:
    grade = "3"
elif points <= 89:
    grade = "4"
else:
    grade = "5"

print("Grade:", grade)