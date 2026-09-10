def check_rotation(list1,list2):
    if len(list1) != len(list2):
        return False 
    
    key_1=list1[0]
    print (key_1)
    Key_loc2=-1
    
    for i in range(len(list2)):
        print ("inside loop"+str(i))
        if list2[i] == key_1:
            Key_loc2=i
            print (Key_loc2)
            break
        
    if Key_loc2 == -1:
        return False 
        
    for i in range(len(list1)):
        j=(Key_loc2+i)%(len(list1))
        if list1[i] != list2[j]:
            return False 
        
    return True 

list1=[1,2,3,4,5,6,7]
list2=[4,5,6,7,1,2,3]

print (check_rotation(list1,list2))
            
        
        