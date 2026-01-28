# Write your solution here
def most_common_character(my_string: str) -> str:
    more_occured = 0
    character = ""
    for char in my_string:
        occurrance = my_string.count(char)
        if occurrance > more_occured:
            more_occured = occurrance
            character = char
    return character

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
