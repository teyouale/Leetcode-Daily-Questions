from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnding = False
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for char in word:
            if char in  node.children:
                node = node.children[char]
            else:
                newNode = TrieNode()
                node.children[char] = newNode
                node = newNode
        node.isEnding = False
        node.count+=1 
        return node.count
class Solution:
    def topKFrequent(self, words: List[str], limit: int) -> List[str]:
        res = defaultdict(int)
        obj = Trie()
        for k,v in enumerate(words):
            c = obj.insert(v)
            res[v] = c
     
        res = Counter(res)
        return[x for x,y in  sorted(res.most_common(), key = lambda x: (-x[1], x[0]))][:limit]