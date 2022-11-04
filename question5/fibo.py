import math as m
def nthNum(n):
    phi=(1+m.sqrt(5))/2
    fn=(pow(phi,n)-pow((-1/phi),n))/m.sqrt(5)
    return int(fn)

def nthfib(a,b,n):
    if n==0:
        return a
    return nthfib(b,a+b,n-1)

##for i in range(50):
##    print(i,"th fibonacci number using formula:",nthNum(i)," \t  using iteration:",nthfib(0,1,i))
