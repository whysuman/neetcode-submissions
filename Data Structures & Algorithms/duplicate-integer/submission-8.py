class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chars = set()
        for indx,integer in enumerate(nums):
            if integer in chars:
                return True
            chars.add(integer)
        return False