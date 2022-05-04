from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ''
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self,word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode()
                node.children[char] = newNode
                node = newNode
        node.word = word
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        # BFS APPROCH
        ans = ""
        bfs = [trie.root]
        while bfs:
            curr = bfs.pop()
            for child in curr.children.values():
                if child.word :
                    if len(child.word) > len(ans) or (len(child.word) == len(ans) and child.word<ans):
                        ans = child.word
                    bfs.append(child)
        return ans
                