# Write a python program to find the factorial of a number using while loop

inp=int(input("ENTER THE FACTORIAL NUMBER TO FIND:"))
facto=1
i=1
while i<=inp: 
    facto*=i
    i+=1
print("THE FACTORIAL OF",inp,"is :",facto)