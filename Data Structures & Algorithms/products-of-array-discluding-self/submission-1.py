class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix*=nums[i]
        print(res)
        suffix = 1
        for j in range(len(nums) - 1,-1,-1):
            res[j] *= suffix
            print(f"Suffix before multiplication: {suffix}")
            suffix *= nums[j]
            print(f"The suffix for the curret number: {nums[j]} is {suffix}")
        print(res)
        return res