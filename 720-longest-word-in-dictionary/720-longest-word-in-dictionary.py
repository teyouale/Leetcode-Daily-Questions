class Solution:
    def longestWord(self, words: List[str]) -> str:
        dct = set()
        words.sort()
        ans = ''
        for word in words:
            if len(word)==1 or word[:-1] in dct:
                dct.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans
        