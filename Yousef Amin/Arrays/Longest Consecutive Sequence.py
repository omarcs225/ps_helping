class Solution:
    def longestConsecutive(self, nums) -> int:
        
        s = set(nums)
        long = 0
        
        for num in nums:
            if num-1 not in s:
                length = 1
                next_num = num+1
                while next_num in s:
                    length+=1
                    next_num+=1
                long = max(long,length)
        return long

