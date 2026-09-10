def powerset(array):
    subsets=[[]]
    for ele in array:
        for i in range(len(subsets)):
            #print (range(len(subsets)))
            currentsubset = subsets[i]
            #print ("currentsubset :"+str(currentsubset))
            subsets.append(currentsubset +[ele])
            #print ("subsets :"+str(subsets))
    return subsets
            
print (powerset([1,2,3]))