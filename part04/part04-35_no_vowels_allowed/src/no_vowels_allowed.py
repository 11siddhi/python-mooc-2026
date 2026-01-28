# Write your solution here
def no_vowels(my_string) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for char in my_string:
        if char in vowels:
            new_string += ""
        else:
            new_string += char

    return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
