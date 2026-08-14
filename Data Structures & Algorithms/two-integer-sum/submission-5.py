class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}
        for i,elem in enumerate(nums):
            diff = target - elem
            if diff in targets and targets[diff] != i:
                return [targets[diff],i]
            targets[elem] = i