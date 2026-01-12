# Write your solution here
gift_value = int(input("Value of gift: "))

if gift_value >= 5000 and gift_value < 25000:
    low_limit = 5000
    tax_limit = 100
    tax_rate = 8
elif gift_value >= 25000 and gift_value < 55000:
    low_limit = 25000
    tax_limit = 1700
    tax_rate = 10
elif gift_value >= 55000 and gift_value < 200000:
    low_limit = 55000
    tax_limit = 4700
    tax_rate = 12
elif gift_value >= 200000 and gift_value < 1000000:
    low_limit = 200000
    tax_limit = 22100
    tax_rate = 15
elif gift_value >= 1000000:
    low_limit = 1000000
    tax_limit = 142100
    tax_rate = 17
else:
    tax_limit = 0
    tax_rate = 0


if gift_value > 5000:
    payable_amt = (tax_limit + (gift_value - low_limit) * (tax_rate/100))
    print(f"Amount of tax: {payable_amt} euros")
else:
    print("No tax!")