import PolyLagIntPol as P
import LagIntPol as L
import NewRaph as NR
import integrate as I
import numpy as np
import mat as M
import check as ch
from sympy import Symbol, diff

##taking [c,b,a,w]
w=Symbol("w")
a=Symbol("a")
b=Symbol("b")
c=Symbol("c")
    
var=[c,b,a]


def coEff(var,n):
    
    
    ##exponential
    ex=[]
    factorial=1
    
    ##So that we just have highest order till n.
    for i in range(n):
        ex.append(pow(w,i)/factorial)
        factorial*=(i+1)
    
    
    var=P.prod(ex,var)
    
    var2=[]
    for i in range(n):
        var2.append(var[i])
        
    return var2
    

def Jac(f,var,n):
    l=[]
    for i in range(n):
        l.append([])
        for j in range(n):
            # print("1\t",l)
            l[i].append(diff(f[i],var[j]))
            # print("2\t",l)
            
    return l


def CoupledNonLinearSysSolverUsingSymbol(func,var,eps):
    n=len(var)+1
    
    f=coEff(var,n)
    
    var.append(w)
    
    for i in range(n):
        f[i]-=func[i]
    
    J=Jac(f,var,n)
    iJ=M.inv(J)
    
    
    # Initial Guess value
    x0=[1,-4,2,0]
    
    return NR.rootFind3(f,iJ,x0,eps)
    
'''
def CoupledNonLinearSysSolverSec(func,A2,eps):

    return NR.sec(func,[2,-3.8,1,0.22],eps,5)
'''

def omega(func,w,n):
    
    sum=0
    factorial=1
    for i in range(n+1):
        sum+=func[n-i]*pow(-w,i)/factorial
        factorial*=(i+1)
        
    return sum

def findABC(func,n,eps):
    ##equate the x^n coeff of func(x)*exp(-wx)=0 to get the value for w
    ##Note: this will give us n different values depending on the initial guess value. Hence we will have to get the right initial guess and check with a plot if its correct
    
    abc=[]
    w0=1
    w1=0.9
    w=NR.rootOmega(func,omega,w0,w1,eps,n)

    ex=[]
    factorial=1
    funcn=[]
    
    ##So that we just have highest order till n.
    for i in range(n):
        ex.append(pow(-w,i)/factorial)
        factorial*=(i+1)
        funcn.append(func[i])
    
    
    vm=P.prod(ex,func)
    
    for i in range(n):
        abc.append(vm[i])

    abc.append(w)
    
    return abc


def run(x_val,y_val,eps,n):
        
    
    func=P.intPol(x_val,y_val)      ##only valid for small values of x. Else the small errors in higher order causes big deviations
    
    # # # The required file for this is in assignment2_RAW, when you run the main from that, you can change it there and see the difference. Not adding one extra file here, when it has no other reason but to just explore lots of new things but not really needed
    '''
    # # # Uncomment this to see the effects of large error propagation due to expanding that 99 degree polynomial in effect
    # ch3.plot(func,x_val,y_val,-1,1)
    # ch3.plot(func,x_val,y_val,-2,1.3)
    # ch3.plot(func,x_val,y_val,-2,2)
    '''
    
    print("The value of the interpolated function at x= 2.5 is ",L.intPol(2.5,x_val,y_val))
    
    r1=NR.rootFind(L.intPol,L.difIntPol,1,x_val,y_val,eps)
    r2=NR.rootFind(L.intPol,L.difIntPol,3.5,x_val,y_val,eps)
    print("The roots of the interpolated functions are around ", r1," and ",r2)
    
    print("The area under the curve from 0 to 4 is ", I.simprule(L.intPol,x_val,y_val,n,0,4))
    
    print("The point x where the integral goes to 0 is ", NR.rootFind2(I.simprule,L.intPol,1,x_val,y_val,eps,n))
    
    A=P.prod([-r1,1],[-r2,1])
    
    print("But since there are no roots to exponential function. The roots corresponds to this particular function (c+bx+ax^2). Hence [c,b,a] are in the ratio ",A)
    print("And from the x=0 case of this polynomial, we get (c+b*0+a*0)*exp(w*0)=c= ", func[0])
    
    t= func[0]/A[0]
    for i in range(len(A)):
        A[i]*=t
    
    print("Therefore [c,b,a] are ",A)
    
    x0=0.05
    sum=0
    for i in range(len(x_val)):
        sum+=func[i]*pow(x0,i)
       
    #value of A at x0
    A0=A[0]+A[1]*x0+A[2]*x0*x0
    
    w=np.log(sum/A0)/x0
    A.append(w)
    
    print("Therefore [c,b,a,w]= ",A)
    
    
    
    
    print()
    print()
    print()
    print()
    
    eps2=pow(10,-15)
    var2=CoupledNonLinearSysSolverUsingSymbol(func,var,eps2)
    print("From Solving the non linear system of equation using Symbol library we get by comparing the coefficients of powers of x (using Newton Raphson Method), we get [c,b,a,w] as ",var2," which is consisten with our previous answer!")
    print("Note: This desnt use root trick!\n\n")
    
        
    ##This 3 says thatw e are looking for first 3 coefficients. If we change it, we can find for other functional forms too. eg ax^3+bx^2+cx+d and so on
    abc=findABC(func,3,eps)
    
    print("From another method, without using Symbols and solving using newton raphson, we get [c,b,a,w]= ",abc)
    print("Note: This doesnt use the root trick or the Symbol library")
    
    ch.plot(A,var2,abc,x_val,y_val)
    
    
    print("\nThe green and red curves are so near that we cant distinguish it unless we zoom in many times!")
    
    '''
    
    A2=[1,-4,2,0]        ##[c,b,a,w]
    
    var3=CoupledNonLinearSysSolverSec(func,A2,eps2)
'''