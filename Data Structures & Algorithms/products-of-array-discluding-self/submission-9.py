class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)

        prefix_curr_prod = 1
        for i in range(len(nums)):
            if i == 0:
                result[i] = 1
                continue
            prefix_curr_prod *= nums[i - 1]
            result[i] = prefix_curr_prod

        curr_prod = 1
        for i in range(len(nums) - 1,-1,-1):
            if i == len(nums) - 1:
                continue
            curr_prod *= nums[i + 1]
            result[i] = result[i]*curr_prod

        return result


            