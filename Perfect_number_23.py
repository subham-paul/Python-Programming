x = int(input("Enter the range= "))

for j in range(x+1):
    sum=0
    m=j//2

    for i in range(1,m+1):
        if j%i==0:
            sum+=i

    if sum==j:
        print(j,end=" ")
