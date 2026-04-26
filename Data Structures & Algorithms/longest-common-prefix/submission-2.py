class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rec = strs[0]
        for x in strs:
            if len(x) < len(rec):
                rec = x


        minimum = 99999
        rec = strs[0]
        for x in strs:
            if len(x) < len(rec):
                rec = x


        minimum = 999999
        for x in strs:
            i = 0
            while (i < len(rec) and rec[i] == x[i]):
                i+=1
            if i < minimum:
                minimum = i

        return rec[0:minimum]