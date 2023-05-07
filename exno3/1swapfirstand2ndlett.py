# Write a Python program to get a single string from two given strings,
# separated by a space, and swap the first characters of each string

str1 = input("ENTER THE FIRST STRING: ")
str2 = input("ENTER THE SECOND STRING: ")
swap_str1 = str2[0] + str1[1:]
swap_str2 = str1[0] + str2[1:]
res = swap_str1 + " " + swap_str2
print("STRINGS AFTER SWAPPING FIRST LETTER:", res)
























# repo created by kerston2104