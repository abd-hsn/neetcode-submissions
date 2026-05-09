class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_list = []
        postfix_list = []
        output = []
        for i in range(len(nums)-1):
            if i==0:
                prev_value =1
                prefix_list.append(1)

            prefix_list.append(prefix_list[i]* nums[i])
        
        for i in range(len(nums)-1):
            if i==0:
                postfix_list.append(1)
            
            postfix_list.append(postfix_list[i] *nums[len(nums)-1-i])

        for i in range(len(nums)):
            prev_value = prefix_list[i]
            post_value = postfix_list[len(nums) - 1 - i]
            output.append(prev_value * post_value)

        return output