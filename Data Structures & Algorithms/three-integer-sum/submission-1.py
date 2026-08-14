class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) ==  3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [[nums[0],nums[1],nums[2]]]
            else:
                return []

        nums.sort()
        final_list = []
        print(nums)
        for indx,val in enumerate(nums):
            if val > 0:
                break
            
            if val == nums[indx - 1] and indx > 0:
                continue
            
            left = indx + 1
            right = len(nums) - 1
            
            print("target: ",-1*val)
            while left < right:
                print(f"left,right: {nums[left]},{nums[right]}")
                if nums[left] + nums[right] == (-1*val):
                    final_list.append([val,nums[left],nums[right]])
                    left += 1
                    right -= 1
                
                elif nums[left] + nums[right] > (-1*val):
                    right-=1

                else:
                    left +=1

                while left < right and nums[left] == nums[left - 1] and left - 1 != indx:
                        left += 1

        return final_list

                

                


 

        return final_list


                
                

        