class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] :
                continue
            if nums[i] > 0:
                return result

            left = i + 1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                total = nums[left] + nums[right] 
                if total < target:
                    temp = nums[left]
                    while temp == nums[left] and left < right:
                        left+=1
                elif total > target:
                    temp = nums[right]
                    while temp == nums[right] and right > i:
                        right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    temp = nums[left]
                    temp2 = nums[right]
                    while temp == nums[left] and left < right:
                        left+=1
                    while temp2 == nums[right] and right > i:
                        right-=1                        
        
        return result


        