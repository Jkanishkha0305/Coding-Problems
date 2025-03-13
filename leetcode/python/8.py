class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  
        i, n, sign, result = 0, len(s), 1, 0
        
        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] in ('-', '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            if result > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX
            
            result = result * 10 + digit
            i += 1
        
        return sign * result