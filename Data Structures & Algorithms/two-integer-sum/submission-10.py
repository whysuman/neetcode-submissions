class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indx_map = {} #we store numbers(keys) and their list position(values) in a dictionary for easy access
        for idx,num in enumerate(nums):
            diff = target - num #we dont have to store diff in memory
            if diff in indx_map.keys(): #Compare if the diff w.r.t the current number is already there in the dict
                return [indx_map[diff],idx] #return the answer
            indx_map[num] = idx #If the diff is not found, then add the current num into the index map
         
