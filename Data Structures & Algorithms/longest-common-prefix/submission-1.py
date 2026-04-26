class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rec = strs[0]
        for x in strs:
            if len(x) < len(rec):
                rec = x


        minimum = 99999
        for x in strs:
            i = 0
            for l in range(len(rec)):
                if(rec[i] == x[l]):
                    i+=1
                else:
                    break
            if i < minimum:
                minimum = i

        return rec[0:minimum]