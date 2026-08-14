class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        curr = nums[0]
        target_indx = 0
        while target_indx < len(nums) - 1: 
            #Gonna use the two pointer approach
            i = target_indx + 1
            target = -1*nums[target_indx]
            j = len(nums) - 1
            curr = nums[i]
            while i < j:
                if nums[i] + nums[j] > target:
                    while j > 1  and nums[j] == nums[j - 1] :
                        j-=1
                    j-=1
                elif nums[i] + nums[j] < target:
                    while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                        i+=1
                    i+=1
                else:
                    result.append([nums[i],nums[j],nums[target_indx]])
                    while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                        i+=1
                    i+=1
                                
            while target_indx < len(nums) - 1 and nums[target_indx] == nums[target_indx + 1]:                    
                target_indx+=1
            target_indx+=1
        return result
            