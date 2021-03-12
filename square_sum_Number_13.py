#square of the natural numbers
x = int (input("Enter the range = "))
sum = 0
for i in range (1,x+1) :
    z = i*i
    print ("Square value of ",i,"is ",z)
    sum = sum + z
print("Sum value = ",sum)
