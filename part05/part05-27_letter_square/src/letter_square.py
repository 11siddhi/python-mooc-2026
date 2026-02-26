# Write your solution here


def letter_square(num: int): 
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  length = num + (num - 1)
  same_char_no = length
  next_let = 1
  start = ""
  end = ""
  for i in range(length):
    print(start + same_char_no * letters[num-next_let] + end)
    if i < (num-1):
      start += letters[num-next_let]
      end = letters[num-next_let] + end
      same_char_no -= 2
      next_let += 1
      
    if i >= (num - 1):
      start = start[:-1]
      end = end[1:]
      same_char_no += 2
      next_let -= 1


# if __name__ == "__main__": 
number = int(input("Enter num: "))
letter_square(number)  