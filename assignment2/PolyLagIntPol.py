
##does product of 2 polynomials
def prod(l1, l2):
    n=len(l1)
    m=len(l2)
    if(n==0 or m==0):
        print("Error!!!")
        return 
        
    
    l=[]
    for i in range(n+m-1):
        l.append(0)
        
    for i in range(n):
        for j in range(m):
            l[i+j]+=l1[i]*l2[j]
            
    return l
    
    
# Performs Addition of two polynomials
def addition(l1,l2):
    l=[]
    i=0
    
    while (i<len(l1) or i<len(l2)):
        if(i>=len(l1)):
            l.append(l2[i])
        elif(i>=len(l2)):
            l.append(l1[i])
        else:
            l.append(l1[i]+l2[i])
            
        i=i+1
        
    return l
    
# Finds Lagrange Polynomials in terms of Polynomial expansion
def intPol(x_val,y_val):

    sum=[]
    for i in range(len(x_val)):
        p=[y_val[i]]
        for j in range(len(x_val)):
            if i!=j:
                
                p=prod(p,[-x_val[j]/(x_val[i]-x_val[j]), 1/(x_val[i]-x_val[j])])
            
        sum=addition(sum,p)
    return sum
