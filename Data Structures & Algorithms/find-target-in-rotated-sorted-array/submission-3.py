class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums) - 1

        

        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        deflection = left

        
        if target >= nums[deflection] and target <= nums[len(nums) - 1]:
            left = deflection
            right = len(nums) - 1
            while left < right:
                mid = (right + left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

        elif target >= nums[0] and target >= nums[deflection]:
            left = 0
            right = deflection
            while left < right:
                mid = (right + left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

        print(nums[left])
        if target == nums[left]:
            return left

        return -1

            
