import sys
import numpy as np
import math
import matplotlib.pyplot as plt

##print(sys)
##print(sys.path)

sys.path.insert(0,"..")

##print()
##print(sys.path)

from question5.fibo import nthNum as form, nthfib as fib


def rform(n):       ##ratio using formula for finding nth fibonacci number
    return form(n+1)/form(n)

def rfib(n):        ##ratio without using formula for finding nth fibonacci number
    return fib(0,1,n+1)/fib(0,1,n)

m=25

x=np.linspace(1,m,m)
##print(x)

y1=[0]*(m)
y2=[0]*(m)

##print(y1)
##print("y2= ",y2)

for i in range(0,m):
    y1[i]=rform((i+1))
    y2[i]=rfib((i+1))

##print(y1)
##print("y2",y2)

fig, ax=plt.subplots(1,2)

ax[0].plot(x,y1,label="ratio")
ax[0].set_xlabel("Number n")
ax[0].set_ylabel("ratio between (n+1)th and nth fibonacci number")
ax[0].set_title("Ratio using form method")
ax[0].legend()


ax[1].plot(x,y2,label="ratio")
ax[1].set_xlabel("Number n")
ax[1].set_ylabel("ratio between (n+1)th and nth fibonacci number")
ax[1].set_title("Ratio using fib method")
ax[1].legend()

plt.show()

print("The answer appraoches the golden ratio, which is (1+sqrt(5))/2= ",((1+math.sqrt(5))/2)," but our last value is ",y1[m-1]," which approaches the golden ratio assymptotically")
