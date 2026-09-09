class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        
        if nums[right] > nums[left]:
            return nums[left]

        while right - left > 1:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

        return min(nums[right],nums[left])

            

            


        
