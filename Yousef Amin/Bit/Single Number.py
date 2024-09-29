class Solution:
    def singleNumber(self, nums) :
        
        s = 0
        
        for num in nums:
            s ^=num
        
        return s