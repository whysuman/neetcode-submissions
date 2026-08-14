class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_before = [0]*len(nums)
        prod_after = [0]*len(nums)
        result = [0]*len(nums)

        curr_prod = 1
        for indx in range(len(nums)):
            if indx == 0:
                prod_before[indx] = curr_prod

            else:
                curr_prod = curr_prod*nums[indx - 1]
                prod_before[indx] = curr_prod


        curr_prod = 1
        for indx in range(len(nums) - 1, -1, -1):
            # print(indx)
            if indx == len(nums) - 1:
                prod_after[indx] = curr_prod
            else:
                curr_prod = curr_prod*nums[indx + 1]
                prod_after[indx] = curr_prod

        print(prod_after)
        for indx in range(len(nums)):
            result[indx] = prod_before[indx]*prod_after[indx]

        return result

            