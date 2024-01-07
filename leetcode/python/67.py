class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        d = []
        for i,j,k,l in zip_longest(a[::-1], range(len(a)), b[::-1], range(len(b)), fillvalue=0): #zip_longest better when 2 variables have different lenths
            m = int(i) << j #similar to (pow(2,j))
            n = int(k) << l #similar to (pow(2,l))
            c += m + n
        if c == 0:
            return ('0')
        while c > 0:
            d.append(str(c%2)) #list append better than concatenating
            c = c // 2
        return ''.join(d[::-1])