class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        if (len(s) % 2 == 0):
            while((j-i) > 0):
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i+=1
                j-=1
        else:
            while(i != j):
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i+=1
                j-=1
