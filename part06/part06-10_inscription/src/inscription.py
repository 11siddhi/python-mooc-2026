# Write your solution here
name = input("Whom should I sign this to: ")
filename = input("Where shall I save it: ") 

with open(filename, "w") as inscription:
  inscription.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")