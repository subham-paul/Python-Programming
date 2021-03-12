n= int(input("Enter value= "))
for i in range (0,n):
    for j in range (0,n-i):
        print(end=" ")
    for j in range (0,i+1):
        print("1", end=" ")
    print("")


"""Enter value= 5
     1 
    1 1 
   1 1 1 
  1 1 1 1 
 1 1 1 1 1
 """
