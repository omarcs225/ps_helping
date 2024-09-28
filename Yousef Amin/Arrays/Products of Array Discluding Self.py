class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prod = 1
        
        for num in nums:
            prod *=num
            
        lst = [0]*len(nums)
        
        for i,value in enumerate(nums):
            if value !=0:
                lst[i] = prod//value
                continue
                
            else:
                s=1
                for j in range(len(nums)):
                    if j!=i :
                        s *=nums[j]
                lst[i] =s
        
        return lst
        
