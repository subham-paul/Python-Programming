#salary calculation
x= float(input("enter your basic salary: "))
DA = 15/100*x
print("DA=",DA)
TA = 10/100*x
print("TA=",TA)
HRA = 30/100*x
print("HRA",HRA)
Gross= x + DA + TA +HRA
print("Gross=",Gross)
PF= 12/100*x
print("PF=",PF)
NET = x - PF
print("NET=",NET)

"""
enter your basic salary: 25000
DA= 3750.0
TA= 2500.0
HRA 7500.0
Gross= 38750.0
PF= 3000.0
NET= 22000.0
"""
