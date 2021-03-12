#calculate the weight charge
x = int(input("enter the weight: "))

if ( x <= 10) :
    print("charge Rs. 20")
if (x>10 and x<=25):
    sum= 20+(x*2)
    print("charge Rs.",sum)
if (x >= 26):
    sum= 50+(x*2)
    print("charge Rs.",sum)
