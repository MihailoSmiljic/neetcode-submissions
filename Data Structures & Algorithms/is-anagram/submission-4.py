class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        for l1 in t:
            if l1 not in s:
                return False
            else:
                s.remove(l1)

        
        return True if (len(s) == 0) else False