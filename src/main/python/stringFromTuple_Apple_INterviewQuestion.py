def can_make_string(pairs, target):
    # Convert the list of pairs into a dictionary of available characters
    available = {}
    for i, (first, second) in enumerate(pairs):
        available.setdefault(first, []).append(i)
        available.setdefault(second, []).append(i)
    print (available)
    used_indices = set()

    for char in target:
        if char not in available:
            return False

        # Find an unused index for this character
        found = False
        for index in available[char]:
            print ("char:"+char)
            print ("index:"+str(index))
            if index not in used_indices:
                used_indices.add(index)
                found = True
                break
        
        print ("here")
        if not found:
            return False

    return True

# Examples
pairs = [("l", "e"), ("u", "t"), ("c", "o")]
#print(can_make_string(pairs, "cul"))  # True
print(can_make_string(pairs, "lut"))  # False
#print(can_make_string(pairs, "leco")) # False
            
        

