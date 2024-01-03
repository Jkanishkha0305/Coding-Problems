class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        a = 0

        for n, i in enumerate(s):
            if n < len(s) - 1 and d[i] < d[s[n + 1]]:
                a -= d[i]
            else:
                a += d[i]
        return a
