x = int (input("Enter the value="))
sum = 0
while (x>0):
    y=x%10
    sum = sum + y
    x=x//10
print("Sum of the value ",sum)
