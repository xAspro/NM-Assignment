
##Returns a copy of the matrix
def copyMat(m):
    n=[]
    for i in range(len(m)):
        n.append([])
        for j in range(len(m[0])):
            n[i].append(m[i][j])
    
    return n

##returns the norm of a vector
def norm(v):
    n=0
    
    for i in range(len(v)):
        
        n+=pow(v[i],2)
        
    return pow(n,(1/2))
    
##Converts row vector to column vector
def transp(vT):
    v=[]
    for i in range(len(vT)):
        v.append([vT[i]])
    
    return v
    
##converts column vector to row vector
def invTransp(v):
    vT=[]
    for i in range(len(v)):
        vT.append(v[i][0])
        
    return vT
    
##subtracts two vectors
def subV(l1,l2):

    l=[]
    for i in range(len(l1)):
            l.append(l1[i]-l2[i])
        
    return l
    
##Multiplies two matrix
def prod(l1,l2):
    klim=len(l1[0])
    if (klim==len(l2)):
        
        l=[]
        for i in range(len(l1)):
            l.append([])
            for j in range(len(l2[0])):
                sum=0
                for k in range(klim):
                    sum+=l1[i][k]*l2[k][j]
                l[i].append(sum)
        
        return l
    print("Some Error!")
    return 
    
##Multiplies a matrix and a vector
def prodMV(m,vT):
    n=len(vT)
    if (n==len(m)):
        # transpose
        v=transp(vT)
        
        return invTransp(prod(m,v))
        
        
##removes a particular row and column from a matrix
def rem(m,k,l):
    n=[]
    i2=0
    for i in range(len(m)):
        if i==k:
            continue
        n.append([])
        for j in range(len(m)):
            if j==l:
                continue
            n[i2].append(m[i][j])
        i2+=1
            
    return n

##Returns the determinant of a matrix
def det(m):
    if len(m)==1:
        return m[0][0]
    
    d=0
    i=0
    
    m1=copyMat(m)
    for j in range(len(m1)):
       n=rem(m1,i,j)
       d+=m1[i][j]*det(n)*pow(-1,(i+j))
        
    return d

##Finds the inverse of a matrix
def inv(m):
    d=det(m)
    if d==0:
        print("Error!!")
        return
    inv=[]
    for i in range(len(m)):
        inv.append([])
        for j in range(len(m)):
            inv[i].append(pow(-1,(i+j))*det(rem(m,j,i))/d)
            
    return inv
    
    
'''
def f(func,A2):
    ex=[]
    factorial=1
    
    ##So that we just have highest order till x.
    for i in range(len(A2)):
        if i!=0:
            factorial*=(i)
        ex.append(pow(A2[3],i)/factorial)
    
    
    w=A2.pop()
    print()
    # print(ex)
    A1=P.prod(ex,A2)
    
    A=[]
    
    # sum=0
    for i in range(len(A2)+1):
        # print(i)
        A.append(A1[i]-func[i])
        # print(A)
        # sum+=A1[i]*pow(x0,i)
        # print(sum)
    
    
    A2.append(w)
    # print(A2)
    # print(A)
    
    return A

def der(func,A2,i):
    h=0.0000001        ##Later Give this as eps/1000 maybe
    
    A21=[]
    A22=[]
    # print("A2=",A2)
    
    for k in range(len(A2)):
        # print("A21=",A21)
        # print("A22=",A22)
        A21.append(A2[k])
        if k!=i:
            A22.append(A2[k])
        else:
            t=A2[k]+h
            print(t)
            A22.append(t)
    # print("A21   =",A21)
    # print("A22   =",A22)
    
    
    v1=f(func,A22)
    v2=f(func,A21)
    val=[]
    # print("v1= ",v1)
    # print("v2= ",v2)
    
    # print("Going to return val!!!")
    for k in range(len(v1)):
        val.append((v2[k]-v1[k])/h)
        # print("val\t\t\t=",val)
    return val

def iJac(func,A2):
    
    f1=f(func,A2)
    # print(f1)
    # print(A2)
    
    print()
    
    J=[]
    
    for i in range(len(A2)):
        J.append(der(func,A2,i))
        
    # print(J)
    
    
    iJ=inv(J)
    
    # print("\n\n\niJ=\t",iJ)
    
    l=prodMV(iJ,f1)
    # print(l)
    
    return l
# iJac([1,1,1,1],[3,2,1,1])

'''