def find_missing_number(full_set,partial_set):
    xor_sum=0
    for num in full_set:
        xor_sum ^= num
        print (xor_sum)
    
    print ("set2")
    for num in partial_set:
        #print (num)
        xor_sum ^= num
        print (xor_sum)
        
    return xor_sum

a = [4,12,9,5,6]
b = [4,12,9,6]
print(find_missing_number(a,b))  # (1,2)