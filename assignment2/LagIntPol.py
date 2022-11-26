## Finds Langrange interpolation for particular i value
def intPolL_i(x,x_val,p,i):
    for j in range(len(x_val)):
        if i!=j:
            p*=(x-x_val[j])/(x_val[i]-x_val[j])
            
    return p

## Finds Langrange interpolation 
def intPol(x,x_val,y_val):
    sum=0
    for i in range(len(x_val)):
        sum+=intPolL_i(x,x_val,y_val[i],i)
    return sum


## Finds differentiation of Langrange interpolation for particular i value
def difIntPolL_i(x,x_val,p,i):
    sum=0
    for j in range(len(x_val)):
        if i!=j:
            sum+=1/(x-x_val[j])
            
    return sum*intPolL_i(x,x_val,p,i)
    
## Finds differentiation of Langrange interpolation 
def difIntPol(x,x_val,y_val):
    sum=0
    for i in range(len(x_val)):
        sum+=difIntPolL_i(x,x_val,y_val[i],i)
    return sum




"""
def coeffForParticularL_i(l,x_val,y_val,i,n):
    
    for k in range(n):
        #for n=0,1,2..
        x_val2=[]
        for j in range(len(x_val)):
            if (i!=j):
                x_val2.append(-x_val[j])
                
        # print("in lagintpol n=0,1,2...     x_val2= ",x_val2)
    
        val=p.coeffFinder(x_val2,k)
    
        coeff=1/y_val[i]
        for j in range(len(x_val)):
            if (i!=j):
                coeff*=(x_val[i]-x_val[j])
            
    
        # l.append([])
    
        l[-1].append([])
    
        l[-1][-1].append(val/coeff)
        
        # print("in n=0,1,2...    l=",l)
    
        # l[i][n][0]=val/coeff
    
        #for n=100,99,98..
        x_val2=[]
        for j in range(len(x_val)):
            if (i!=j):
                x_val2.append(-1/x_val[j])
        
        # print("in lagintpol n=0,1,2...     x_val2= ",x_val2)
        val=p.coeffFinder(x_val2,k)
    
        prod=1
        for j in range(len(x_val)):
            prod*=x_val[j]

        coeff=pow(-1,len(x_val2))*x_val[i]/(y_val[i]*prod)
        for j in range(len(x_val)):
            if (i!=j):
                coeff*=(x_val[i]-x_val[j])
            
        # l.append([[]])
        # l[i][n][0]=val/coeff

        # l.append([])
    
        # l[-1].append([])
    
        l[-1][-1].append(val/coeff)
    
        # print(l)
        
        
        
    

def coeffIntPol(x_val,y_val,n):
    l=[]
    for i in range(len(x_val)):
    
        # print("\t\t\t\t\t\tL_i= ",i)
        l.append([])
        coeffForParticularL_i(l,x_val,y_val,i,n)
        
        # print()
        # print()
        # print(l)
        
    # print()
    # print()
    # print(l)
        
    n1=[]
    n2=[]
    for i in range(len(l[0])):
        sum1=0
        sum2=0
        
        for j in range(len(l)):
            sum1+=l[j][i][0]
            sum2+=l[j][i][1]
            
        n1.append(sum1)
        n2.append(sum2)
        
    
    # print(n1)
    # print(n2)
    

coeffIntPol([1,2,3],[2,2,2],3)
# coeffIntPol([1,2,3,4],[1,2,3,4],2)
# coeffForParticularL_i([],[1,2,3,5],[1,2,3,4],0,2)


"""
