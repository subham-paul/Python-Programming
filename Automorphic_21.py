N = int(input("Enter the value= "))
def isAutomorphic(N) :  
    sq = N * N 
    while (N > 0) :
        if (N % 10 != sq % 10) :
            return False
        N /= 10
        sq /= 10
    return True

if isAutomorphic(N) : 
    print ("Automorphic")
else : 
    print  ("Not Automorphic")
