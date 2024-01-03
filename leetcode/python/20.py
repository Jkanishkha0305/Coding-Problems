class Solution:
    def isValid(self, s: str) -> bool:
        flag = 0 
        d = { ')': '(', '}': '{',']': '['}
        stack = []
        for i in s  :
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if not stack or stack.pop() != d[i]:
                    return False
                
        return not stack
                