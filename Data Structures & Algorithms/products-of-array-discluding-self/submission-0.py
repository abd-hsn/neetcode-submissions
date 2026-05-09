class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = []
        for i,num1 in enumerate(nums):
            p=1
            for j,num2 in enumerate(nums):
                if i == j:
                    continue
                p = p*num2
            answers.append(p)
        return answers