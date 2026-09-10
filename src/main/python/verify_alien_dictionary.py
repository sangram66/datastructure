
class Solution:
    
    def compare(self, cache, word1, word2):
        i, j = 0,0
        while i < len(word1) and j < len(word2):
            if cache[word1[i]] < cache[word2[j]]:
                return True
            elif cache[word1[i]] > cache[word2[j]]:
                return False
            else: #letters equal case
                i += 1
                j += 1
                
        print (i,j,len(word1),len(word2))

        if i < len(word1):
            return False
        """
            why false?
            In some cases word1 can be aaa, word2 can be aa
            here we must return false becoz they are not in lexicographic order
            becoz word2 appears first than word1
        """
        
        return True #same words case and shorter words case like aa, aaa i will definitely reach end 
    
    def isAlienSorted(self, words, order) :
        """
            Main Idea behind this is,
            How we see our Oxford or Some english Dictionary (So called lexicographic order)
            
            Eg:
            Case 1:
                Assume we have words like ad, af, ag, ba, bba, bbaaaag in our oxford Dictionary
                at diff page numbers Now compare the page numbers of these words once it is for sure
                pageNumber(ad) < pageNumber(af) < pageNumber(ag) < ... pageNumber(bbaaag)
            Case 2:
                if we go in depth
                if two 2 words are in same page, say x, xy
                it is for sure LineNumber(x) < lineNumber(xy) (Note < operator is Strictly lesser)
            Case 3:
                Words like a, aa, aaa, aaaa are in our dictionary
                definitly appearance(a) < appearance(aa) < appearance(aaa) < appearance(aaaa)
                appearance may be a line number or page number
        """
        
        """
            In our Question there are asking for a different alphabetical order and asking us to check 
            whether appearance(word1) < appearance(word2) < appearance(word3) < ... < appearance(wordn) or not
            Just compare 
                word1 with word2 
                word2 with word3
                word3 with word4
                ....
                wordn-1 with wordn
            Reason: if word1 < word2 it is for sure lesser than word3 and so on
        """
        cache = {}
        
        for i in range(len(order)):
            cache[order[i]] = i
        

        print (cache)
        for i in range(1, len(words)):
            if not self.compare(cache, words[i-1], words[i]):
                return False
        return True
    
'''   
words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
'''

words =["aaa","aa"]
order ="ngxlkthsjuoqcpavbfdermiywz"

print (Solution().isAlienSorted(words,order))
 
''' 
class Solution:
    def isAlienSorted(self, words, order):
        indexes = {}
        for i, c in enumerate(order):
            indexes[c] = i
        ans = True
        i = 0
        while ans and i < len(words) - 1:
            print ("i: "+str(i))
            for a, b in zip(words[i], words[i+1]):
                print (f"{a},{b} "+str(a),str(b))
                if a == b: 
                    print ('continue')
                    continue
                print (indexes[b] , indexes[a])
                if indexes[b] > indexes[a]: 
                    print ('break')
                    break
                ans = False
            else:
                print ('else')
                if len(words[i]) > len(words[i+1]): ans = False
            i += 1
        return ans
    

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

words = ["kuvp","qo"]
order = "ngxlkthsjuoqcpavbfdermiywz"
 
words =["apple","app"]
order ="abcdefghijklmnopqrstuvwxyz"

words =["word","world","row"]
order ="worldabcefghijkmnpqstuvxyz"
print (Solution().isAlienSorted(words,order))
''' 

