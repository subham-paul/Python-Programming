#Additional subject
x = int(input("Bengali= "))
y = int(input("English= "))
z = int(input("Math= "))
A = int(input("Computer= "))
sum=0
sum=(x+y+z+A)-34
avg = sum//3
print("result",sum)
print("average",avg)

if (avg > 80):
    print("S")
if (avg > 70 and avg < 79):
    print("A")
if (avg > 60 and avg < 69):
    print("B")
if (avg >= 50 and avg < 59):
    print("C")
if (avg < 50):
    print("F")



