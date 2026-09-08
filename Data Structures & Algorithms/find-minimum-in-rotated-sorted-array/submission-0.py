class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0, len(nums) - 1

        while nums[left] > nums[right]:
            if nums[left] < nums[right]:
                break
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        print(nums[left],nums[right])
        return min(nums[left],nums[right])

        
