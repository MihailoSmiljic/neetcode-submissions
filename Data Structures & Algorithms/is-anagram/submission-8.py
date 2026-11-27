class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapa1 = {}
        c = 0
        if len(s) != len(t):
            return False

        for i in s:
            if i not in mapa1.keys():
                mapa1[i] = 1
            else:
                mapa1[i] += 1

        for i in t:
            if i not in mapa1.keys() or mapa1[i] == 0:
                c = 1
            else:
                mapa1[i] -= 1

        if c != 0:
            return False
        else:
            return True