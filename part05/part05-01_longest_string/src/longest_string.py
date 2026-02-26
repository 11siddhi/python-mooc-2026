# Write your solution here

# can assume there's just one longest string
def longest(strings: list) -> str:
    longest_str = ""
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string
    return longest_str


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))