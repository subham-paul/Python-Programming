"""n = int(input("Check the number: "))
sum = 0
temp = n

while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if n == sum:
   print(n,"is an Armstrong number")

else:
   print(n,"is not an Armstrong number")"""

#USER DEFINED
lower = int (input("Lower range= "))
upper = int (input("Upper range= "))

for num in range (lower, upper + 1):
   order = len(str(num))
   sum = 0
   temp=num

   while temp > 0:
      digit = temp % 10
      sum += digit ** order
      temp //= 10

   if num == sum:
      print(num)
