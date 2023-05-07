# TO FIND THE NO OF UPPER LOWER AND SPACE 

def count(string):
    up=0
    lo=0
    sp=0
    for ele in string:
        if ele.isupper():
            up+=1
        elif ele.islower():
            lo+=1
        elif ele==' ':
            sp+=1
    print(up,"NO OF UPPERCASE")
    print(lo,"NO OF LOWER CASE")
    print(sp,"NO OF BLANK SPACE")

string=input("ENTER THE STRING:")
count(string)

















# repo created by kerston2104