class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = [i for i in range(len(haystack)) if haystack[i:i+len(needle)] == needle]
        if k:
            return k[0]
        else:
            return -1