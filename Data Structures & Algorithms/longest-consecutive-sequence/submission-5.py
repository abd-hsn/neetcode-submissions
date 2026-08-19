import math
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Create the set!
        #have a list of n*n where it contains the subtraction,
        if len(nums) == 0:
            return 0
        set_numbers = nums
        set_numbers.sort()
        consecutive = 1
        max_consecutive = 1
        for i,num in enumerate(set_numbers):
            if i+1 == len(set_numbers):
                break

            diff = math.fabs(num - set_numbers[i+1])
            if diff ==1:
                consecutive+=1
            elif diff ==0:
                continue
            else:
                if max_consecutive < consecutive:
                    max_consecutive=consecutive
                consecutive=1
        if max_consecutive < consecutive:
            return consecutive
        else:
            return max_consecutive
            