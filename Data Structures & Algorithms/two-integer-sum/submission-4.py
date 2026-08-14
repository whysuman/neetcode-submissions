class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test_target = target
        target_dict = {}
        for ind,elem in enumerate(nums):
            target_dict[elem] = ind

        for i,elem in enumerate(nums):
            diff = target - elem
            if diff in target_dict and target_dict[diff] != i:
                return [i,target_dict[diff]]
