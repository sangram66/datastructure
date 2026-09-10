import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.mapp=collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.mapp:
            rlt=self.mapp[key]
            self.mapp.pop(key)
            self.mapp[key]=rlt
            return rlt
        else: return -1

    def put(self, key: int, value: int) -> None:
        self.mapp.pop(key,None)
        self.mapp[key]=value
        if len(self.mapp)>self.capacity:
            self.mapp.popitem(last=False)
        
'''       
cache=LRUCache(0)
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       #// returns 1
cache.put(3, 3);    #// evicts key 2
cache.get(2);       #// returns -1 (not found)
cache.put(4, 4);    #// evicts key 1
cache.get(1);       #// returns -1 (not found)
cache.get(3);       #// returns 3
cache.get(4);       #// returns 4
'''
cache=LRUCache(2)
cache.put(1, 1) 
print(cache.mapp) 
cache.put(2, 2) 
print(cache.mapp) 
cache.get(1) 
print(cache.mapp) 
cache.put(3, 3) 
print(cache.mapp) 
cache.get(2) 
print(cache.mapp) 
cache.put(4, 4) 
print(cache.mapp) 
cache.get(1) 
print(cache.mapp) 
cache.get(3) 
print(cache.mapp) 
cache.get(4) 
print(cache.mapp) 