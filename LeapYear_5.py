#Checked the year leap or not
year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")

"""
Enter year to be checked:2019
The year isn't a leap year!
"""
