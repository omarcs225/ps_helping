class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        return sorted(nums,reverse=True)[k-1]