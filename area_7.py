print("press 1 for Area of Square \npress 2 for Area of Rectangle \npress 3 for Area of Triangle")

x = int(input("Your choice: "))

def square():
    a=int (input("enter the value of area= "))
    area=a*a
    print("Area of square= ",area)

def rectangle():
    a=int (input("enter the value of lenght= "))
    b=int (input("enter the value of width= "))
    area=a*b
    print("Area of rectangle= ",area)

def triangle():
    a=int (input("enter the value of length= "))
    b=int (input("enter the value of width= "))
    area=(a*b)/2
    print("Area of triangle= ",area)

dictionary ={
    1 : square,
    2 : rectangle,
    3 : triangle}
dictionary.get(x)()
    
