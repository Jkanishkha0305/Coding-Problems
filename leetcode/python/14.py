class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        o = ""
        for chars in zip(*strs):
            if all(char == chars[0] for char in chars): o += chars[0]
            else: break
        return o