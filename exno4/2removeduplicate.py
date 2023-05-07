# Write a Python program to remove duplicate elements in a list.

inp = input("Enter a list of elements separated by commas: ").split(",")
unilist = []
for elem in inp:
    if elem not in unilist:
        unilist.append(elem)
print("List with duplicates removed:", unilist)


















# repo created by kerston2104