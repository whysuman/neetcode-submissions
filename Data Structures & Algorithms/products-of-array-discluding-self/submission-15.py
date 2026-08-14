class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        product = 1
        for index,num in enumerate(nums): 
            if index == 0:
                result[index] = product
                continue
            product = product*nums[index - 1]
            result[index] = product

        # print(prefix)
        product = 1
        for index in range(len(nums) - 1,-1,-1):
            if index == len(nums) - 1:
                continue
            product = product*nums[index + 1]
            result[index] *= product

        return result
            