from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        return[x for x,y in  sorted(c.most_common(), key = lambda x: (-x[1], x[0]))[:k]]