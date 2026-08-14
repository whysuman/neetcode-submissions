class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i,elem in enumerate(nums):
            if elem not in duplicate:
                duplicate[elem] = i
            else:
                return True
        return False
