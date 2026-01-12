# Write your solution here
year = int(input("Year: "))
leap = year
found = False
while not found:
    leap += 1
    if leap % 4 == 0:
        if leap % 100 == 0:
            if leap % 400 == 0:
                found = True
                break
        else:
            found = True
            break
    
print(f"The next leap year after {year} is {leap}")