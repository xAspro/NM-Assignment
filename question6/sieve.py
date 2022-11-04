import math
import numpy as np

def s(n):
    a=[True]*(n+1)      ##as array starts from 0 
##    print(a)

    for i in range(2,n+1):
##        print("i = ",i)
        if a[i]:
##            print("in")
            j=2*i
            while j<=n:
                a[j]=False
                j+=i

    for i in range(2,n+1):
        if a[i]:
            print(i)
##    print(a)

s(200)
