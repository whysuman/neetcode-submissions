class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #no explicit constraints given
        #base case -- only one number
        #GOTCHAS -- NO SPECIFIC GOTCHAS RIGHT NOW
        num_map = {}
        for indx,num in enumerate(nums):
            print(num_map.keys())
            if num in num_map:
                return True
            num_map[num]  = indx

        
        return False

