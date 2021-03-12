list=[10,20,30,40,50,60]
print("Max no in the list = ", max(list))
print("Min no in the list = ", min(list))
x = max(list)
y = min(list)
list.remove(x)
list.remove(y)
print()
print("2nd max no in the list = ", max(list))
print("2nd min no in the list = ", min(list))

"""
Max no in the list =  60
Min no in the list =  10

2nd max no in the list =  50
2nd min no in the list =  20
"""
