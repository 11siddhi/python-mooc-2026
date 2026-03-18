# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total_sum = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.total_sum += number

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        return self.total_sum
    
    def average(self):
        if self.numbers == 0:
            return 0
        return self.total_sum/self.numbers


stats = NumberStats()
odd_stats = NumberStats()
even_stats = NumberStats()
while True:
    num = int(input("Please type in integer numbers: "))
    if num != -1:
        stats.add_number(num)
        if num % 2 == 0:
            even_stats.add_number(num)
        else:
            odd_stats.add_number(num)
    else:
        break 

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even_stats.get_sum())
print("Sum of odd numbers:", odd_stats.get_sum())



