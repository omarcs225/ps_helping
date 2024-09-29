class Solution:
    def missingNumber(self, nums) :
        
        my_set = set(nums)
        
        for num in nums:
            if num != 0 and num-1 not in my_set:
                return num-1
        
        return max(nums)+1