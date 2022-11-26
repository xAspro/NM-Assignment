

# def intPol(x,x_val,y_val):
    # sum=0
    # for i in range(len(x_val)):
        # p=y_val[i]
        # for j in range(len(x_val)):
            # if i!=j:
                # p*=(x-x_val[j])/(x_val[i]-x_val[j])
            
        # sum+=p
    # return sum


def prod(l1, l2):
    n=len(l1)
    m=len(l2)
    if(n==0 or m==0):
        print("Error!!!")
        return 
        
    
    """
    l=[l1[0]*l2[0]]
    
    #Since we are just using l2 to as a linear polynomial, we can directly just do this alone
    #else we will have to make sure we take all sums were l[i]=l1[j]l[k], where i=j+k
    
    for i in range(len(l1)-1):
        l.append(l1[i]*l2[1]+l1[i+1]*l2[0])
        
    l.append(l1[-1]*l2[-1])
    
    print(l)
    # return l
    
    """
    
    
    l=[]
    for i in range(n+m-1):
        l.append(0)
        
    for i in range(n):
        for j in range(m):
            l[i+j]+=l1[i]*l2[j]
            
    # print(l)
    return l
    
    
    
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
        
    # print(l)
    return l
    

def intPol(x_val,y_val):

    # print("In PolyLagIntPol")
    # print("x=",x_val)
    # print("y=",y_val)
    
    sum=[]
    for i in range(len(x_val)):
        # print("i= ",i)
        p=[y_val[i]]
        for j in range(len(x_val)):
            # print("j=      ",j)
            if i!=j:
                # p*=(x-x_val[j])/(x_val[i]-x_val[j])
                
                p=prod(p,[-x_val[j]/(x_val[i]-x_val[j]), 1/(x_val[i]-x_val[j])])
            
        # sum+=p
        sum=addition(sum,p)
    # print(sum)
    return sum

# prod([1,2,3],[1,2])