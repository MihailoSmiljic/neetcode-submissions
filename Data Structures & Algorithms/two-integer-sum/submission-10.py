# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:    
#         # for i in range(len(nums)):
#         #     for j in range(len(nums)):
#         #         if (i != j and nums[j] == (target - nums[i])):
#         #             return [i , j]

#         indices = {}
#         for i , n in enumerate(nums):
#             indices[n] = i
        
#         for i , n in enumerate(nums):
#             diff = target - n
#             if diff in indices and diff != n :
#                 return [i , indices[diff]]
            
        



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
        
        

        