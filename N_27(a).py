x=int(input("Enter the number of term = "))
next=0
for i in range(1,x+1):
    next=i*(i+1)//2
    print(next,end=" ")
    print()

"""
Enter the number of term = 10
1 
3 
6 
10 
15 
21 
28 
36 
45 
55
"""
