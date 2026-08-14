class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #no explicit constraints given
        #base case -- only one number
        #GOTCHAS -- NO SPECIFIC GOTCHAS RIGHT NOW
        seen = set()
        for indx,num in enumerate(nums):
            print(seen)
            if num in seen:
                return True
            seen.add(num)

        
        return False

