def getlocations(string,substring):
    locations=[]
    startidx=0
    while startidx < len(string):
        nextidx=string.find(substring,startidx)
        if nextidx != -1:
            locations.append([nextidx,nextidx + len(substring)])
            startidx = nextidx+1
        else:
            break
    print ("getlocations   "+str(locations))
    return locations

def collapse(locations):
    if not len(locations):
        return locations
    newlocations =[locations[0]]
    previous = newlocations[0]
    print ("newlocations before before  "+str(newlocations))
    for i in range(1,len(locations)):
        current=locations[i]
        if current[0] <= previous[1]:
            previous[1] = current[1]
            print ("previous   "+str(previous))
            print ("current   "+str(current))
        else:
            print ("newlocations before  "+str(newlocations))

            newlocations.append(current)
            print ("newlocations   "+str(newlocations))
            previous = current
            
    print ("collapse   "+str(newlocations))
    return newlocations

def underscorify(string,locations):
    locationsidx=0
    stringidx=0
    inbetweenunderscore = False
    finalchars=[]
    i=0
    while stringidx < len(string) and locationsidx < len(locations):
        print ("locationsidx "+str(locationsidx))
        if stringidx == locations[locationsidx][i]:
            finalchars.append("_")
            inbetweenunderscore = not inbetweenunderscore
            if not inbetweenunderscore:
                print ("inbetweenunderscore "+str(inbetweenunderscore))
                print ("locationsidx "+str(locationsidx))
                locationsidx += 1
            i=0 if i==1 else 1
        print ("stringidx: "+str(stringidx))
        finalchars.append(string[stringidx])
        stringidx += 1
    if locationsidx < len(locations):
        finalchars.append("_")
    elif stringidx < len(string):
        finalchars.append(string[stringidx:])
    return "".join(finalchars)
    
    
string="this is a test to see if it works and test"
substring="test"
locations =  collapse(getlocations(string,substring))
print (underscorify(string,locations))
    