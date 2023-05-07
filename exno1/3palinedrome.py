# Write a python program to check whether the number is palindrome or not

inp=input("ENTER THE NUMBER :")
str_inp=str(inp)
rev_str_inp=str_inp[::-1]
if inp==rev_str_inp:
    print("THE GIVEN VALUE IS A PALINEDROME")
else:
    print("THE GIVEN VALUE IS NOT A PALINEDROME")