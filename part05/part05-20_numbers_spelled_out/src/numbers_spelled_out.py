# Write your solution here
def dict_of_numbers() -> dict:
  ones = ['zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']

  twos = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

  tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
          'seventy', 'eighty', 'ninety']
  spelled_num = {}
  for i in range(0, 100):
    if i < 10:
      spelled_num[i] = ones[i]
    elif i < 20:
      spelled_num[i] = twos[i%10]
    elif i % 10 == 0:
      spelled_num[i] = tens[(i//10)-2]
    else:
      word = f"{tens[(i//10)-2]}-{ones[i%10]}"
      spelled_num[i] = word
  return spelled_num
  
if __name__ == "__main__":
  numbers = dict_of_numbers()
  print(numbers[2])
  print(numbers[11])
  print(numbers[45])
  print(numbers[99])
  print(numbers[0])

