class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for l in range(len(nums)):
            for n in nums[l+1:]:
                if nums[l] == n:
                    return True
        return False