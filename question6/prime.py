import math

def f(n):
#    print(math.sqrt(n))
#    print(int(math.sqrt(n)))
    print()
    for j in range(2,n):
        flag=True
        for i in range(2,int((math.sqrt(j)+1))):
#            print("This is j: ",j, "  and range :",int((math.sqrt(j)+1)))
            if j%i==0:
#                print("j= ",j,"    i= ",i)
                flag=False            
        if flag:
            print(j," ")
#       print("2This is i: ",i)

f(200)
    
