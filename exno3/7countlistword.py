# Write a Python program to find characters count of a string which are passed as list.

inp=input("ENTER THE STRING: ")
list_char=list(input("ENTER THE CHARACTER TO COUNT: "))
count=0
for char in inp:
    if char in list_char:
        count+=1
print("THE OUTPUT IS ",count)















# repo created by kerston2104