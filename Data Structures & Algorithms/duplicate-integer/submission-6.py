class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encountered = []
        for number in nums:
            if number in encountered:
                return True
            encountered.append(number)
        return False