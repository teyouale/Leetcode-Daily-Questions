from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
            wordDict = defaultdict(list)
            
            for i in words:
                wordDict[i[0]].append(i)
            count = 0
            for i in s:
                wordX = wordDict[i]
                wordDict[i] = []
                for j in wordX:
                    if len(j) == 1:count+=1
                    else:
                        wordDict[j[1]].append(j[1:])
                        
            return count