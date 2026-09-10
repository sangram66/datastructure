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
    print ("seen: 2"+str(seen))
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
       
       
