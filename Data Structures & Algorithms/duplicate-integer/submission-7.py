class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encountered = set()
        for number in nums:
            if number in encountered:
                return True
            encountered.add(number)
        return False