num=int(input("enter the number:"))
numstr=str(num)
n=len(numstr)
sumofdig=0
for ele in numstr:
    sumofdig+=int(ele)**n
if sumofdig==num:
    print(num,"is amstrong")
else:
    print("it is not a amstrong")


















    # repo created by kerston2104