class Student:
    studentcount=0
    def __init__(self, name, roll, s1, s2, s3):
        self.name = name
        self.roll = roll
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def display(self):
        print ("Name : " , self.name , "\nRoll : " , self.roll ,  "\nC lang = " , self.s1 , "\nJava lang = " , self.s2 , "\nPython lang = " , self.s3 )
        self.total=self.s1+self.s2+self.s3
        self.per=self.total//3
        print("Total =", self.total, "\nPer =", self.per)

name= input("Student name=")
roll= int(input("Student roll=")) 
x=int(input("Marks of C lang="))
y=int(input("Marks of Java lang="))
z=int(input("Marks of Python lang="))

student1=Student(name,roll,x,y,z)
student1.display()

"""
Student name=subham
Student roll=56
Marks of C lang=88
Marks of Java lang=98
Marks of Python lang=95
Name :  subham 
Roll :  56 
C lang =  88 
Java lang =  98 
Python lang =  95
Total = 281 
Per = 93
"""
