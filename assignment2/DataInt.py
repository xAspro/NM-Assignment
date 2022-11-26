import PolyLagIntPol as P
import LagIntPol as L
import NewRaph as NR
import integrate as I
import numpy as np
import mat as M
import check as ch
from sympy import Symbol, diff

# import check3 as ch3

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
    
    ##So that we just have highest order till x.
    for i in range(n):
        ex.append(pow(w,i)/factorial)
        factorial*=(i+1)
    
    
    var=P.prod(ex,var)
    # print("var= ",var)
    
    var2=[]
    for i in range(n):
        var2.append(var[i])
        
    # print(var2)
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
    # print(f)
    
    J=Jac(f,var,n)
    iJ=M.inv(J)
    
    # print("J= ",J)
    # print("iJ= ",iJ)
    
    # print("determinant=   ",M.det(J))
    # print("in DATAINTf= ",f)
    # print("var= ",var)
    # print("func= ",func)
    
    
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
    
    # print(w)
    
    
    ex=[]
    factorial=1
    funcn=[]
    
    ##So that we just have highest order till x.
    for i in range(n):
        ex.append(pow(-w,i)/factorial)
        factorial*=(i+1)
        funcn.append(func[i])
    
    
    vm=P.prod(ex,func)
    # print("var= ",var)
    
    for i in range(n):
        abc.append(vm[i])
    
    # print(abc)
    
    abc.append(w)
    
    return abc


def run(x_val,y_val,eps,n):
    
    # # x_val=[1,2,3,4,5,6,7,8,9,10]
    # # y_val=[1,2,30,4,5454,7,8,45654611,13443,40000025436547654]
    # # func=P.intPol([1,2,3,4,5],[1,2,3,4,5])
    # # func=P.intPol(x_val,y_val)
    
    # func=[2, -3.36, 0.2118, 0.134, 0.05, -0.054, -0.63532, 0.75465, 6.5, -6.307558, -39.63673, 34.605, 162.95712, -132.28766, -478.4485636, 369.77557, 1050.25, -786.331, -1786.286, 1305.375233, 2407, -1751, -2649.5, 1893.453, 2369.728, -1754.572, -1841.153, 1274.9, 1112.29, -870, -584.5, 597.7, 488.8758, 17.4915, 144.026, 329.969, 210.92, 57.8871, 14.05, -7.5365, -37.8381, -47.492, -37.0222, -24.1251, -14.779, -8.041, -3.6596, -1.43, -0.5, -0.139, -0.0145557, 0.01319, 0.01187, 0.007, 0.003567, 0.00159, 0.000627, 0.000221, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    # func=P.intPol(x_val,y_val)
    # print(func)
    
    # val=2.58335
    # sum=0
    # for i in range(len(x_val)):
        # sum+=func[i]*pow(val,i)
        
    # print("sum through sum= ",sum)
    
    
    # print("val through IntPol",L.intPol(val,x_val,y_val))
    
    # val=-0.6
    # sum=0
    # for i in range(len(x_val)):
        # sum+=func[i]*pow(val,i)
        
    # print("sum through sum= ",sum)
    
    # print("val through IntPol",L.intPol(val,x_val,y_val))
    
    # val=0.4
    # sum=0
    # for i in range(len(x_val)):
        # sum+=func[i]*pow(val,i)
        
    # print("sum through sum= ",sum)
    
    # print("val through IntPol",L.intPol(val,x_val,y_val))
    
    
    
    func=P.intPol(x_val,y_val)      ##only valid for small values of x. Else the small errors in higher order causes big deviations
    # # # Uncomment this to see the effects of large error propagation due to expanding that 99 degree polynomial in effect
    # ch3.plot(func,x_val,y_val,-1,1)
    # ch3.plot(func,x_val,y_val,-2,1.3)
    # ch3.plot(func,x_val,y_val,-2,2)
    
    print("The value of the interpolated function at x= 2.5 is ",L.intPol(2.5,x_val,y_val))
    
    # m=1000
    # for i in range(m):
        # n=3.1+(3.3-3.1)/m*i
        # print("n= ",n,"   L.intPol=",L.intPol(n,x_val,y_val))
    
    r1=NR.rootFind(L.intPol,L.difIntPol,1,x_val,y_val,eps)
    r2=NR.rootFind(L.intPol,L.difIntPol,3.5,x_val,y_val,eps)
    print("The roots of the interpolated functions are around ", r1," and ",r2)
    
    print("The area under the curve from 0 to 4 is ", I.simprule(L.intPol,x_val,y_val,n,0,4))
    
    print("The point x where the integral goes to 0 is ", NR.rootFind2(I.simprule,L.intPol,1,x_val,y_val,eps,n))
    
    # print("\n\nOrder comparison:\nLagrange Polynomial= ",func)
    # print("Note: each ith element corresponds to the coefficient of x^i")
    # print()
    # print("Taking the first 4 values and solving by hand, we get an intuitive idea on how the solution might look like. In fact we get 3 valid solutions from these 4 equations. Added the workings in the answer script")
    
    A=P.prod([-r1,1],[-r2,1])
    # print("A= ",A)
    
    print("But since there are no roots to exponential function. The roots corresponds to this particular function (c+bx+ax^2). Hence [c,b,a] are in the ratio ",A)
    print("And from the x=0 case of this polynomial, we get (c+b*0+a*0)*exp(w*0)=c= ", func[0])
    
    # sum=0
    # for i in range(len(x_val)):
        # sum+=func[i]*pow(0.2,i)
    # print(sum,"   ",L.intPol(0.2,x_val,y_val))
    
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
    # print("A0= ",A0)
    
    w=np.log(sum/A0)/x0
    # print(w)
    A.append(w)
    
    print("Therefore [c,b,a,w]= ",A)
    
    
    
    
    print()
    print()
    print()
    print()
    
    # # x=Symbol('x')
    # # y=Symbol('y')
    
    # # exp=x**2+y**2
    # # print(exp)
    # # print(diff(exp,x))
    
    
    ##taking [c,b,a,w]
    # w=Symbol("w")
    # a=Symbol("a")
    # b=Symbol("b")
    # c=Symbol("c")
    
    # var=[c,b,a]
    
    eps2=pow(10,-15)
    var2=CoupledNonLinearSysSolverUsingSymbol(func,var,eps2)
    print("From Solving the non linear system of equation using Symbol library we get by comparing the coefficients of powers of x (using Newton Raphson Method), we get [c,b,a,w] as ",var2," which is consisten with our previous answer!")
    print("Note: This desnt use root trick!\n\n")
    
    
    # print("This is the guessed method from manipulating the roots")
    # ch.plot(A,x_val,y_val)
    # print("This is the function we get from Numerically solving the nonlinear system of equation")
    # ch.plot(var2,x_val,y_val)
    
    
    
    # print(J)
    
    # print("var= ",var)
    # print("func= ",func)
    
    
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