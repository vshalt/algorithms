"""
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).
"""

def string_compression(string):
    counter = 0
    compressed = []

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i] + str(counter))
            counter = 0
        counter += 1

    if counter:
        compressed.append(string[-1] + str(counter))

    return min(string, "".join(compressed), key=len)
