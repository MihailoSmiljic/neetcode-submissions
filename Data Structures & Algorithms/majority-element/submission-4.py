class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        cons = len(nums) // 2
        repeated_time = 1
        curr = nums[0]
        maximum = -9999999999
        most = -99999999
        # for i in range(len(nums)):
        #     if nums[i] in dictionary:
        #         dictionary[nums[i]] += 1  
        #         if(dictionary[nums[i]] > cons):
        #             return nums[i]
               
        #     else:
        #         dictionary[nums[i]] = 1
        #     if(dictionary[nums[i]] > maximum):
        #         maximum = nums[i]

        # return maximum
        #1 1 1 5 5 5 5
        for i in range(1 , len(nums)):

            if nums[i] == curr:
                repeated_time += 1
            else:
                if repeated_time > most:
                    maximum = curr
                    most = repeated_time
                
                repeated_time = 1
                curr = nums[i]
        if repeated_time > most:
                maximum = curr
                most = repeated_time    

        if most > cons:
            return maximum
                

            
