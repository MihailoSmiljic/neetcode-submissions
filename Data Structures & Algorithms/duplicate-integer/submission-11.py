class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        mapa = {}
        for el in nums:
            if el not in mapa:
                mapa[el] = 1
                continue
            return True
        return False