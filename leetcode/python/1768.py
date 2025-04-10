class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=[]
        A,B = len(word1), len(word2)
        a,b = 0,0
        word = 1

        while a<A and b<B:
            if word == 1:
                x.append(word1[a])
                a += 1
                word = 2
            else:
                x.append(word2[b])
                b += 1
                word = 1
            
        while a<A:
            x.append(word1[a])
            a += 1

        while b<B:
            x.append(word2[b])
            b += 1
        
        return ''.join(x)
