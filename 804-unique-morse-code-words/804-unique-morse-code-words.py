class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hashTable = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = set()
        for word in words:
            temp = []
            for c in word:
                x = ord(c)-97
                temp.append(hashTable[x])
            trans.add(''.join(temp))
        return len(trans)
                