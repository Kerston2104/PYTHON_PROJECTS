# Write a Python program to find characters count of a string which are passed as list.

string = input("Enter a string: ")
chars = input("Enter characters to count (separated by space): ").split()

char_count = {char: string.count(char) for char in chars}

for char, count in char_count.items():
    print(f"{char}: {count}")
















# repo created by kerston2104