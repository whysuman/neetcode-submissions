class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        indx = 0
        result = []
        while indx < len(nums) - 1:
            i = indx + 1
            j = len(nums) - 1
            target = -1*nums[indx]
            while i < j:
                three_sum = nums[i] + nums[j]
                if three_sum < target:
                    i+=1
                elif three_sum > target:
                    j-=1
                else:
                    result.append([nums[indx],nums[i],nums[j]])
                    i+=1
                    j-=1
                    while nums[i] == nums[i - 1] and i < j:
                        i+=1
            while indx < len(nums) - 1 and nums[indx] == nums[indx + 1]:
                indx+=1  
            indx+=1
        return result
            