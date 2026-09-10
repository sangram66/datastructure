
def flatten(current, key, result):
    #print (current,key)
    if isinstance(current, dict):
        for k in current.keys():
            print ("key: "+k)
            new_key = "{0}.{1}".format(key, k) if len(key) > 0 else k
            flatten(current[k], new_key, result)
    else:
        print (current,key)
        result[key] = current
        print (result)
    return result

my_dict = {'a': 1,
     'c': {'a': 2, 'b': {'x': 5, 'y' : 10}},
     'd': [1, 2, 3]}

flat = flatten(my_dict, '', {})

print (flat)


'''
dictA = {
   "id": "0001",
   "name": "hotdog",
   "image":
      {
         "url": "images/0001.jpg",

            "thumbnail":
               {
                  "url": "images/thumbnails/0001.jpg",
                  "height,width": "2x4"
               }
      }
}

def dict_flatten(in_dict, dict_out=None, parent_key=None, separator="_"):
   if dict_out is None:
      dict_out = {}

   for k, v in in_dict.items():
      k = f"{parent_key}{separator}{k}" if parent_key else k
      if isinstance(v, dict):
         dict_flatten(in_dict=v, dict_out=dict_out, parent_key=k)
         continue

      dict_out[k] = v

   return dict_out

dictA = {'a': 1,
     'c': {'a': 2, 'b': {'x': 5, 'y' : 10}},
     'd': [1, 2, 3]}
final_dict = dict_flatten(dictA)
print(final_dict)
'''
