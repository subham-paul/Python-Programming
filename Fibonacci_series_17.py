#fibonacci series
a,b=0,1
n = int (input("limit= "))
while(a<=n):
    print(a, end=" ")
    a = a + b
    b = a - b
