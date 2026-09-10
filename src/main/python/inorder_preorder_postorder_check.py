'''
Input : Inorder -> 4 2 5 1 3
        Preorder -> 1 2 4 5 3
        Postorder -> 4 5 2 3 1
Output : Yes
Exaplanation : All of the above three traversals are of 
the same tree.             1
                         /   \
                        2     3
                      /   \
                     4     5

Input : Inorder -> 4 2 5 1 3
        Preorder -> 1 5 4 2 3
        Postorder -> 4 1 2 3 5
Output : No

1.Search for the first element of preorder array in the inorder array and store it’s index as idx, if it doesn’t exist then return False.
2.Everything from 0th index for inorder and postorder and from 1st index for preorder of length idx becomes left subtree for first element of the preorder array.
3.Everything from position idx+1 for inorder and preorder and from idx for postorder of length (length-idx-1) becomes right subtree for first element of preorder array.
4.Repeat the steps 1 to 3 recursively until length of arrays become either 0 (in which case we
return true) or 1 (in which case we return True only if all three arrays are equal, else False).

--ret1 = checktree(preorder[1:], inorder, postorder, idx); 
--ret2 = checktree(preorder[idx + 1:], inorder[idx + 1:], postorder[idx:], length-idx-1); 

'''

# Python program to check if the given  
# three traversals are of the same  
# tree or not 
  
# Function to check if all three traversals 
# are of the same tree 
def checktree(preorder, inorder, postorder, length): 
      
    # if the array lengths are 0,  
    # then all of them are obviously equal 
    if length == 0:  
        return 1
          
    # if array lengths are 1,  
    # then check if all of them are equal 
    if length == 1:  
        return (preorder[0] == inorder[0]) and (inorder[0] == postorder[0]); 
  
    # search for first element of preorder  
    # in inorder array 
    idx = -1; 
      
    for i in range(length): 
        if inorder[i] == preorder[0]: 
            idx = i 
            break
      
    if idx == -1: 
        return 0; 
      
    # check for the left subtree 
    print ("for ret1: preorder,inorder,postorder,length "+str(preorder[1:]),str(inorder),str(postorder),str(idx))  
    ret1 = checktree(preorder[1:], inorder, postorder, idx); 
      
    # check for the right subtree   
    print ("for ret2: preorder,inorder,postorder,length,idx,sent "+str(preorder[idx + 1:]),str(inorder[idx + 1:]),str(postorder[idx:]),str(length),str(idx),str(length-idx-1))  
    ret2 = checktree(preorder[idx + 1:], inorder[idx + 1:],  
                           postorder[idx:], length-idx-1); 
      
    # return 1 only if both of them are correct else 0 
    return (ret1 and ret2) 
  
# Driver Code 
if __name__ == "__main__": 
    inorder = [4, 2, 5, 1, 3]  
    preorder = [1, 2, 4, 5, 3]  
    postorder = [4, 5, 2, 3, 1] 
    len1 = len(inorder) 
    len2 = len(preorder) 
    len3 = len(postorder) 
  
    # check if all the array lengths are equal 
    if (len1 == len2) and (len2 == len3): 
        correct = checktree(preorder, inorder,  
                                postorder, len1) 
        if (correct):  
            print("Yes")  
        else:  
            print("No") 
    else: 
        print("No"); 