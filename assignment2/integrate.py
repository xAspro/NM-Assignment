def simpruledA(f,x_val,y_val,a,b):
    return (b-a)*(f(a,x_val,y_val)+4*f((a+b)/2,x_val,y_val)+f(b,x_val,y_val))/6

def simprule(f,x_val,y_val,n,a,b):
    h=(b-a)/n
    sum=0
    
    for i in range(n):
        # print(sum)
        sum+=simpruledA(f,x_val,y_val,a+h*i,a+h*(i+1))
        
    return sum
    
def simpruledA2(f,a,b):
    return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6

def simprule2(f,n,a,b):
    h=(b-a)/n
    sum=0
    
    for i in range(n):
        # print(sum)
        sum+=simpruledA2(f,a+h*i,a+h*(i+1))
        
    return sum
    
    
def traprule(f,n,a,b):
    h=(b-a)/n
    sum=(f(a)+f(b))/2
    for i in range(n-1):
        # print(sum)
        sum+=f(a+(i+1)*h)
        
    return sum*h
    
    
"""
def f(x):
    return x
    
print("sum= ",traprule(f,10,0,10))
print("sum= ",simprule(f,10,0,10))

"""