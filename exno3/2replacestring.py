# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to ‘#’ except the first char
# itself.

inp=input("ENTER THE STRING:")
letter1=inp[0]
rep_letter=inp.replace(letter1,"#")
res=letter1 + rep_letter[1:]
print("MODIFIED STRING : ",res)


















# repo created by kerston2104