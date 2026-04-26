class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return True if (not(len(set(nums)) == len(nums))) else False 

        return not(len(set(nums)) == len(nums))