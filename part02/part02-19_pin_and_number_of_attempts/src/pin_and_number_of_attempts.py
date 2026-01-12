# Write your solution here
pin = int(input("PIN: "))
actual_pin = 4321
attempts = 1
while pin != actual_pin:
    attempts += 1
    print("Wrong")
    pin = int(input("PIN: "))

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")