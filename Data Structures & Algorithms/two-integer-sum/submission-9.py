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
            
        



from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(0, len(nums)):
            x = nums[i]
            if x not in dict:
                dict[x] = []
            dict[x].append(i)

        for broj in dict.keys():
            r = target - broj
            if r == broj:
                if len(dict[r]) > 1:
                    return [dict[broj][0], dict[broj][1]]
                else:
                    continue
            if r in dict.keys():
                return [dict[broj][0], dict[r][0]]
        
        

        