'''
Time Complexity: O(M×N) : search time reduces to half, since the two parallel searches meet somewhere in the middle.
Space Complexity: O(M×N) : bidirectional reduces the search space. It narrows down because of meeting in the middle.
'''
import string
import collections

def ladderLength(beginWord, endWord, wordList):
    # We use q to keep track of the next nodes to process in the BFS.
    # Each item in the queue is a list with two items:
    #   item[0] = word
    #   item[1] = steps to reach word + 1 (i.e. number of nodes in list of nodes 
    #             traversed to reach word - (format of Word Ladder I output)).
    q = collections.deque([ [beginWord,1] ])
    # We keep track of words we've processed to avoid getting stuck in a loop.
    seen = set([beginWord])
    print ("seen: "+str(seen))
    # wordList is given as a list but we want O(1) lookup so we convert to a set.
    wordList = set(wordList)
    print ("wordlist: "+str(wordList))
    while q:
        q_item = q.popleft()
        print ("---------------------------")
        print ("\n")
        print ("q_item: "+str(q_item))
        for candidate in generateNeighbors(q_item[0], wordList):
            print ("******************************")
            print ("candidate: "+str(candidate)+"       q_item[0]:  "+str(q_item[0]))
            if candidate == endWord:
                print ("return q_item[1] + 1 : "+str(q_item[1] + 1))
                return q_item[1] + 1
            elif candidate in seen:
                continue
            seen.add(candidate)
            print ("seen.add(candidate) : "+str(seen))
            q.append([candidate, q_item[1] + 1])
            print ("q.append([candidate, q_item[1] + 1]) : "+str(q))
    return str(0)      

def generateNeighbors(word, wordList):
    for i in range(len(word)):
        for letter in string.ascii_lowercase:
            candidate = word[:i] + letter + word[i+1:]
            if candidate in wordList:
                print ("generateNeighbors for:  "+str(word)+"     is candidate:  "+str(candidate))
                yield (candidate)

word='hit'
endWord = "cog"
wordList=["hot","dot","dog","lot","log","cog"]
print (ladderLength(word, endWord, wordList))
       
   
'''

Time Complexity: 
O(M×N), where 
M is the length of words and  N is the total number of words in the input word list. Finding out all the transformations takes  M iterations for each of the  N words. Also, breadth first search in the worst case might go to each of the  N words.

Space Complexity: 
O(M×N), to store all 
M transformations for each of the  N words, in the all_combo_dict dictionary. Visited dictionary is of  N size. Queue for BFS in worst case would need space for all  N words.

import collections
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()      
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

if __name__ == "__main__":
    sol=Solution()
    word='hit'
    endWord = "cog"
    wordList=["hot","dot","dog","lot","log","cog"]
    print (sol.ladderLength(word, endWord, wordList))

'''    
