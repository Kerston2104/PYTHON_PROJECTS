# Write a python program to check whether the number is palindrome or not using function

def pali(inp):
    str_inp=str(inp)
    rev_str_inp=str_inp[::-1]
    if inp==rev_str_inp:
        print("THE GIVEN VALUE IS A PALINEDROME")
    else:
        print("THE GIVEN VALUE IS NOT A PALINEDROME")

inpu=input("ENTER THE NUMBER :")
pali(inpu)

















# repo created by kerston2104