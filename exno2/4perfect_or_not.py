# TO FIND THE GIVE NUMBER IS A PERFECT NUMBER

def perf(inp):
    my_list=[]
    for i in range(1,inp):
        if inp%i==0:
            my_list.append(i)
    if sum(my_list)==inp:
        print(inp,"PERFECT NUMBER")
    else:
        print(inp,"IS NOT A PERFECT NUMBER")

inpu=int(input("ENTER THE NUMBER:"))
perf(inpu)