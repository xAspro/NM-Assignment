import readData as rD
import DataInt as dI


def run():

    ##File name and access permission can be changed here
    file_name= r"data.dat"
    access="r"
    
    #root bound (ie. the error for root) and integration number of steps can be changed
    eps=0.0000001
    n=100
    
    
    xy=rD.readFile(file_name,access)
    
    x=[]
    y=[]
    for i in range(len(xy)):
        x.append(float(xy[i].split()[0]))
        y.append(float(xy[i].split()[1]))
        # print(xy[0].split())
    
    # print(x)
    # print(y)
    
    dI.run(x,y,eps,n)
    
    
    # x=x[::4]
    # y=y[::4]
    
    # dI.run(x,y,eps,n)

    
run()