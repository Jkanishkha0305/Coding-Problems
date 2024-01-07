class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = s.split()[-1]
        return len(k)