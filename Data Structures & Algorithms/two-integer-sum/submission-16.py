class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #MAIN CONSTRAINT -- HAS EXACTLY ONE PAIR OF INPUT THAT SATISFIES OF THE TARGET SUM
        #CONSIDER INPUT = [0,-1,5,7] target = -1
        indx_map = {}
        for indx, num in enumerate(nums):
            complement = target - num
            if complement in indx_map:
                return [indx_map[complement], indx]
            indx_map[num] = indx

