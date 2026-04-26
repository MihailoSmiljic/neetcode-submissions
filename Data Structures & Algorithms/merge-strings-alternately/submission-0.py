class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        if(len(word1) >= len(word2)):
            kraca = word2
            duza = word1
        else:
            duza = word2
            kraca = word1

        i = 0
        s = ''
        while(i < len(kraca)):
            s = s + word1[i] + word2[i]
            i+=1
        s += duza[i:len(duza)]

        return s