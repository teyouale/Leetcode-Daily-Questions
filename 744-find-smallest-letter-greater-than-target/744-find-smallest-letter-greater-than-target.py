class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect.bisect(letters,target)
        n = len(letters)
        return letters[i % n]
