class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapa = {}
        for el in nums:
            if el not in mapa:
                mapa[el] = 1
                continue
            return True
        return False