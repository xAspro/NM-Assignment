import integrate as I
from math import log

def f(x):
    return x*log(x)-x
    
    
s=[I.simprule2(f,1,1,3),I.simprule2(f,10,1,3),I.simprule2(f,100,1,3),I.simprule2(f,1000000,1,3)]
t=[I.traprule(f,1,1,3),I.traprule(f,10,1,3),I.traprule(f,100,1,3),I.traprule(f,1000000,1,3)]
print("n=1")
print("simpson rule -->\t",s[0])
print("trapizoidal rule -->\t",t[0])
print("n=10")
print("simpson rule -->\t",s[1])
print("trapizoidal rule -->\t",t[1])
print("n=100")
print("simpson rule -->\t",s[2])
print("trapizoidal rule -->\t",t[2])
print("n=1000000")
print("simpson rule -->\t",s[3])
print("trapizoidal rule -->\t",t[3])


print("\n\nConsidering the n=10^6 value as the true value and checking the error percentage for both the values(Note: here even though I know simpson rule is giving better value, both by theory and by calculating the real value by calculating analytical values and computing the numerical value by calculating, I am still not using it, because in general all we can do when we dont know the real value is, take highest n possible and assume its as close as we want and say thats almost our real value, any lower precision can be calculated with respect to this)\n And here, I am using n=10^6 instead of 1000, because 10^6 will definitely have a huge order of accuracy compared to 1000, so for practical purposes, we can say for looking at error percent of n=1, 10 and 100, n=10^6 is a benchmark with almost the same accuracy as the real value itself")

##error in s
ers=[(s[3]-s[0])/s[3]*100,(s[3]-s[1])/s[3]*100,(s[3]-s[2])/s[3]*100]
ert=[(t[3]-t[0])/t[3]*100,(t[3]-t[1])/t[3]*100,(t[3]-t[2])/t[3]*100]

print("\n\nTherefore the error values are \nSimpson\nn=1\t\t",ers[0],"%\nn=10\t\t",ers[1],"%\nn=100\t\t",ers[2],"\nTrapezoidal\nn=1\t\t",ert[0],"%\nn=10\t\t",ert[1],"%\nn=100\t\t",ert[2])
