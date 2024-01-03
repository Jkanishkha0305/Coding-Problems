class Solution:
    def isPalindrome(self, x: int) -> bool:
        t = x
        n = 0
        while x:
            k = x % 10
            n = n*10 + k
            x = int(x/10)
        if t == n:
            return True
        else :
            return False 
