class Overloading_Area:
    def area (self, a=None, b=None, pi=None):
        if (b is None and pi is None):
            print('Area of Square is : %d' % (a*a))
        elif(pi is None):
            print('Area of Rectangle is : %d' % (a*b))
        else:
            print('Area of Cylinder is : %d' % (2*pi*a*b + 2*pi*a*a))

obj = Overloading_Area()
obj.area(5)
obj.area(5,6)
obj.area(5,6,3.142)
