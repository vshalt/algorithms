"""
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.

EXAMPLE
Input: " Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
"""

def urlify(string: str, true_length: int) -> str:
    result = []
    for i in range(true_length):
        if string[i] == " ":
            result.append("%20")
        else:
            result.append(string[i])
    return "".join(result)

def urlify_pythonic(string: str) -> str:
    return string.rstrip().replace(" ", "%20")
