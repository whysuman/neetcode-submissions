class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod = [1]
        rightprod = [1]

        curr_prod = 1
        for i in range(len(nums) - 1):
            curr_prod *= nums[i]
            leftprod.append(curr_prod)

        curr_prod = 1
        for i in range(len(nums) - 1,-1,-1):
            curr_prod *= nums[i]
            rightprod.append(curr_prod)


        res = []

        for i in range(len(nums)):
            res.append(leftprod[i]*rightprod[len(nums) - i - 1])

        return res


            