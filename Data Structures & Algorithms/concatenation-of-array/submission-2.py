class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums *2
        # ans = nums + nums
        # l = len(nums)
        # ans = [0]*(l*2)
        # for i in range(l*2):
        #     idx = i//l
        #     if idx ==0:
        #         ans[i]=nums[i]
        #     elif idx==1:
        #         ans[(i%l)+l]=nums[i%l] 
                       
        return ans