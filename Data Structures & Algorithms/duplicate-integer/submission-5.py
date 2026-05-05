class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i,num in enumerate(nums):
            for j in range(i+1,len(nums)):
                if num - nums[j]==0:
                    return True
        return False