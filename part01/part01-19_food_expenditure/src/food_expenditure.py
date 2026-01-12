# Write your solution here
time_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery_price = float(input("How much money do you spend on groceries in a week? "))
total_cafetaria_cost = (time_per_week/7) * lunch_price
total_grocery_cost = grocery_price / 7
daily = total_cafetaria_cost + total_grocery_cost
weekly = daily * 7

print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")