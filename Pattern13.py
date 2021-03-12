n = int (input("Enter the height= "))
k=-3
for i in range (n,0,-1):
    for j in range(1,i+1):
        print("%02d "%j,end="")
    for j in range(1,k+1):
        print("#",end="")
    if (i==n):
         j=i-1
    else:
        j=i
    for j in range (j,0,-1):
        print("%02d "%j,end="")
    print("")
    k+=6
k-=6
for i in range (1,n+1):
    for j in range(1,i+1):
        print("%02d "%j,end="")
    for j in range(1,k+1):
        print("#",end="")
    if (i==n):
         j=i-1
    else:
        j=i
    for j in range (j,0,-1):
        print("%02d "%j,end="")
    print("")
    k-=6
"""Enter the height= 5
01 02 03 04 05 04 03 02 01 
01 02 03 04 ###04 03 02 01 
01 02 03 #########03 02 01 
01 02 ###############02 01 
01 #####################01 
01 #####################01 
01 02 ###############02 01 
01 02 03 #########03 02 01 
01 02 03 04 ###04 03 02 01 
01 02 03 04 05 04 03 02 01
"""
