class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapa = []
        for el in nums:
            if el not in mapa:
                mapa.append(el)
                continue
            return True
        return False