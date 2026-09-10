'''
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        print (self.trie)
        cur = self.trie
        print (cur)
        for w in word:
            if w not in cur:
                cur[w] = {}
                print (cur)
            cur = cur[w]
            print (cur)
        cur["#"] = {}
        print (cur)
        print (self.trie)

    def search(self, word) -> bool:
        def _search(word, trie):
           # print (word)
            #print (trie)
            if not word:
                return "#" in trie

            if word[0] == ".":
                return any(_search(word[1:], v) for v in trie.values())
            if word[0] not in trie:
                return False
            return _search(word[1:], trie[word[0]])

        return _search(word, self.trie) 
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
            

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode()
                node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = [(self.root, word)]
        
        while stack:
            node, word = stack.pop()
            
            if not word:
                if node.isEnd:
                    return True
            
            elif word[0] in node.children:
                temp = node.children[word[0]]
                stack.append((temp, word[1:]))
            
            elif word[0] == '.':
                for temp in node.children.values():
                    stack.append((temp, word[1:]))
        
        return False



# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("mad")
obj.addWord("dad")
obj.addWord("them")
obj.addWord("the")

print(obj.search("pad"))
#print(obj.search("bad"))
#print(obj.search(".ad"))
#print(obj.search("b.."))