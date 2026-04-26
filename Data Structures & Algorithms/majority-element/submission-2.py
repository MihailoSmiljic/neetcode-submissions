class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cons = len(nums) / 2
        dictionary = {}
        maximum = -999999
        for i in range(len(nums)):
            if nums[i] in dictionary:
                dictionary[nums[i]] += 1  
                if(dictionary[nums[i]] > cons):
                    return nums[i]
               
            else:
                dictionary[nums[i]] = 1
            if(dictionary[nums[i]] > maximum):
                maximum = nums[i]

        return maximum
            
