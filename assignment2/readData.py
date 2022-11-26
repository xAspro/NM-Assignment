##Reads file and returns its data
def readFile(name,access):

    File =open(name,access)

    xy=File.readlines()
    
    return xy
