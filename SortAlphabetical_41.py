"""str=input("Enter Your Word = ")
x=str.split()
print(x)
x.sort()
print(x)
for i in x:
    print(i, end=" ")"""

"""
Enter Your Word = i am subham
['i', 'am', 'subham']
['am', 'i', 'subham']
am i subham"""

str=input("Enter Your Word = ")
x=str.split()
x.sort()
for i in x:
    print(i, end=" ")

"""
Enter Your Word = i am subham
am i subham 
"""
