class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        # subtracted = [target]*l
        mask = {}
        for i,v in enumerate(nums):
            mask[target - v]=i
        
        for i,n in enumerate(nums):
            v = mask.get(n,-1)
            if v!=-1 and i!=v:
                return [i,v]

        #--------------------------------
        ##Time Complexity --> O(n^2)
        ##Space Complexity --> O(1)
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    return [i,j]