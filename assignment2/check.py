import matplotlib.pyplot as plt
import math as m
import numpy as np

# Returns the functional form given 
def f(x,A):
    return (m.exp((A[3])*x))*((A[2])*x**2+(A[1])*x+A[0])
    

# Plots the graphs
def plot(A,var2,abc,x_val,y_val):
    
    x_1=np.linspace(-5,5,10000)
    y_1=[]
    y_2=[]
    y_3=[]
    for i in range(len(x_1)):
        y_1.append(f(x_1[i],A))
        y_2.append(f(x_1[i],var2))
        y_3.append(f(x_1[i],abc))



    plt.scatter(x_val,y_val)
    plt.plot(x_1,y_1,'b',x_1,y_2,'r',x_1,y_3,'g')
    plt.legend(["Data Points","By root trick","Using Symbol Library","By Newton Raphson"])
    plt.xlabel("x_values")
    plt.ylabel("y_values")
    plt.show()
    