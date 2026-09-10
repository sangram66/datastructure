import string
import collections
import copy
class WordLadder:
    def __init__(self, beginWord):
        self.ladder = [ [beginWord] ]

    def LastWord(self):
        # All lists in self.ladder have to have the same last word
        return self.ladder[0][-1]

    def Merge(self, other):
        self.ladder += other.ladder

    def AppendWord(self, word):
        for x in self.ladder:
            x.append(word)

    def toOutputFormat(self):
        return self.ladder
    
    def generateNeighbors(self,word, wordList):
        for i in range(len(word)):
            for letter in string.ascii_lowercase:
                candidate = word[:i] + letter + word[i+1:]
                if candidate in wordList:
                    print ("generateNeighbors for:  "+str(word)+"     is candidate:  "+str(candidate))
                    yield (candidate)

    
    def allShortestLadders(self,beginWord, endWord, wordList):
    # Each item in the queue is a list of WordLadders (which is just a list of lists
    # that represent a path to get to the same word).
        q = collections.deque([ WordLadder(beginWord) ])
    # We keep track of words we've processed to avoid getting stuck in a loop.
        seen = set([beginWord])
        wordList = set(wordList)
        output = None
        while q:
        # We can't return as soon as we see an answer because we want to
        # return ALL shortest paths. We'll process level by level and only
        # return when we're done a full level.
            num_in_level = len(q)
        # We need to be able to merge two wordLadders so we keep word -> ladder
            seen_this_level = {}
            for i in range(num_in_level):
                q_item = q.popleft()
                for candidate in self.generateNeighbors(q_item.LastWord(), wordList):
                    if candidate in seen:
                        continue
                    newLadder = copy.deepcopy(q_item)
                    newLadder.AppendWord(candidate)
                    if candidate == endWord:
                        if output:
                            output.Merge(newLadder)
                        else:
                            output = newLadder
                    elif candidate in seen_this_level:
                        seen_this_level[candidate].Merge(newLadder)
                    else:
                        seen_this_level[candidate] = newLadder
                        q.append(newLadder)
            if output:
                break
            seen |= [seen_this_level.viewkeys()]
        return output.toOutputFormat() if output else []

if __name__ == '__main__':
    beginWord='hit'
    endWord = "cog"
    wordList=["hot","dot","dog","lot","log","cog"]
    print (WordLadder(beginWord).allShortestLadders(beginWord, endWord, wordList))
       
