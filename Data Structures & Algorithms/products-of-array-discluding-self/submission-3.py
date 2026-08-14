class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod = [1]
        rightprod = [1]

        curr = nums[0]
        for indx in range(1,len(nums)):
            num = nums[indx]
            leftprod.append(curr) 
            print(curr,num)
            curr*=num
        print(leftprod)

        curr = nums[-1]
        for indx in range(len(nums) - 2, -1,-1):
            num = nums[indx]
            rightprod.append(curr)
            curr*=num
            
        print(rightprod)
        final_res = []
        for indx,left in enumerate(leftprod):
            right = rightprod[len(rightprod) - 1 - indx]
            final_res.append(left*right)

        return final_res
            