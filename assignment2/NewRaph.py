import mat as M
import copy
from sympy import *

###Created this to check whats the problem with substituting just for one expression. but later found out, my copying method was still creating a copy by reference object
# def check():
    # x=Symbol('x')
    # y=Symbol('y')
    
    # exp=x**2+y**2
    # exp2=x*y
    # print(exp)
    # print(diff(exp,x))
    # print(exp2)
    
    # exp=exp.subs([(x,5),(y,2)])
    # print(exp)
    # print(diff(exp,x))
    # print(exp2)
    
    # return 
# check()


##Different method finds, root for different argumented functions and all of them performs Newton Raphson


def rootFind(f,dfdx,x,x_val,y_val,eps):
    l=0
    while(True):
        l=f(x,x_val,y_val)/dfdx(x,x_val,y_val)
        x=x-l
        if(abs(l)<abs(eps)):
            break
            
    return x
    
    
def rootFind2(f,dfdx,x,x_val,y_val,eps,n):
    l=0
    while(True):
        l=f(dfdx,x_val,y_val,n,0,x)/dfdx(x,x_val,y_val)
        x=x-l
        if(abs(l)<abs(eps)):
            break
            
    return x
    
def rootFind3(f,iJ,x,eps):
    
    while(True):
        iJ2=copy.deepcopy(iJ)
        f2=copy.deepcopy(f)

        
        for i in range(len(iJ2)):
            for j in range(len(iJ2)):
                iJ2[i][j]=iJ2[i][j].subs([('c',x[0]),('b',x[1]),('a',x[2]),('w',x[3])])
            f2[i]=f2[i].subs([('c',x[0]),('b',x[1]),('a',x[2]),('w',x[3])])
        
        l=M.prodMV(iJ2,f2)
        
        x=M.subV(x,l)
        
        n=M.norm(l)
        if (n<abs(eps)):
            break
           
    return x
    
##This is for finding w value in exp(wx)
def rootOmega(func,f,w0,w1,eps,n):
    while(True):
        tempw1=w1
        l=f(func,w1,n)*(w1-w0)/(f(func,w1,n)-f(func,w0,n))
        w1=w1-l
        w0=tempw1
        
        if(abs(l)<abs(eps)):
            break
            
    return w1
    
'''

# This method alone performs a modified Newton Raphson method, which is Secant method
def sec(func,A2,eps,cnt):

    # print("Before func=   ",func)
    # print("Before A2=   ",A2)
    l=M.iJac(func,A2)
    # print("After A2=   ",A2)
    # print("After l=   ",l)
    
    A2=M.subV(A2,l)
    
    # print(A2)
    
    n=M.norm(l)
    print("n=  ",n)
    
    if(cnt==0):
        return
    if(n<abs(eps)):
        return A2
        
    sec(func,A2,eps,cnt-1)
    
    
'''