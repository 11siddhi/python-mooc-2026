# Write your solution here
def histogram(string: str):
  histogram = {}
  for letter in string:
    if letter not in histogram:
      histogram[letter] = 0
    histogram[letter] += 1
  for letter, times in histogram.items():
    print(letter, times*"*")

if __name__ == "__main__":
  histogram("abba")
