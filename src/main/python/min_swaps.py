def minSwaps(arr): 
    n = len(arr) 
      
    # Create two arrays and use  
    # as pairs where first array  
    # is element and second array 
    # is position of first element 
    arrpos = list(enumerate(arr)) 
      
    # Sort the array by array element  
    # values to get right position of  
    # every element as the elements  
    # of second array. 
    #arrpos.sort(key = lambda it:it[1]) 
    arrpos1=sorted(arrpos, key=lambda x:x[1]) 
    print (arrpos1) 
    # To keep track of visited elements.  
    # Initialize all elements as not  
    # visited or false. 
    vis = {k:False for k in range(n)} 
    print (vis)
    # Initialize result 
    ans = 0
    for i in range(n): 
        print ("i : "+str(i))  
        # alreadt swapped or  
        # alreadt present at  
        # correct position 
        if vis[i] or arrpos1[i][0] == i: 
            continue
              
        # find number of nodes  
        # in this cycle and 
        # add it to ans 
        cycle_size = 0
        j = i
        print ("j : "+str(j)) 
        while not vis[j]: 
              
            # mark node as visited 
            vis[j] = True
            print (vis)  
            # move to next node 
            j = arrpos1[j][0] 
            print ("j2   : "+str(j))   
            cycle_size += 1
            print ("cycle_size   : "+str(cycle_size))    
        # update answer by adding 
        # current cycle 
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    # return answer 
    return ans 
  
# Driver Code      
arr = [1, 5, 4, 3, 2] 
print(minSwaps(arr)) 