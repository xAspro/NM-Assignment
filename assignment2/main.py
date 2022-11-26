import readData as rD
import DataInt as dI


def run():

    ##File name and access permission can be changed here
    file_name= r"data.dat"
    access="r"
    
    #root bound (ie. the error for root) and integration number of steps can be changed
    eps=pow(10,-12)
    n=100
    
    
    xy=rD.readFile(file_name,access)
    
    x=[]
    y=[]
    for i in range(len(xy)):
        x.append(float(xy[i].split()[0]))
        y.append(float(xy[i].split()[1]))
    
    
    dI.run(x,y,eps,n)
    
    
run()