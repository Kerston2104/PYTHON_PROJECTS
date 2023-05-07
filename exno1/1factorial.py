inp=int(input("ENTER THE FACTORIAL NUMBER TO FIND:"))
facto=1
for i in range(1,inp+1):
    facto*=i
print("THE FACTORIAL OF",inp,"is :",facto)