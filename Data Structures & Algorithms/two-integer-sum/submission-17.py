class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_track = {}
        for i in range(len(nums)):
            if target - nums[i] in num_track.keys():
                return [num_track[target - nums[i]] , i]
            num_track[nums[i]] = i 