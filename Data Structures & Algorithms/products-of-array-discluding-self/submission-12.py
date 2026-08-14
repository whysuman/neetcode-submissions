class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        product = 1
        for index,num in enumerate(nums): 
            if index == 0:
                prefix.append(product)
                continue
            product = product*nums[index - 1]
            prefix.append(product)

        # print(prefix)
        product = 1
        for index in range(len(nums) - 1,-1,-1):
            if index == len(nums) - 1:
                suffix.append(product)
                continue
            product = product*nums[index + 1]
            suffix.append(product)

        # print(suffix)
        result = [0]*len(nums)
        for index in range(len(nums)):
            result[index] = prefix[index]*suffix[len(nums) - index - 1]

        return result
            