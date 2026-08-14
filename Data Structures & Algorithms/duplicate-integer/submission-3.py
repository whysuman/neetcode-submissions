class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i,value in enumerate(nums):
            if value not in duplicate:
                duplicate[value] = i
            else:
                return True
        return False