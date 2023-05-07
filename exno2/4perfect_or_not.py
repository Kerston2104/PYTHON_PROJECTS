# TO FIND THE GIVE NUMBER IS A PERFECT NUMBER

inp=int(input("ENTER THE NUMBER:"))
my_list=[]
for i in range(1,inp):
    if inp%1==0:
        my_list.append(i)
        if sum(my_list)==inp:
            print(inp,"PERFECT NUMBER")
    else:
        print(inp,"IS NOT A PERFECT NUMBER")