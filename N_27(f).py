n=int (input("Enter number of term= "))
sum=0
a=5
for i in range(1,n+1):
    print(a)
    sum=sum+a
    a=(a*10)+5
print("Sum of the total number = %ld"%sum)

"""
Enter number of term= 5
5
55
555
5555
55555
Sum of the total number = 61725
"""
