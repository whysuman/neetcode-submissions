class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_indx = defaultdict(list)
        for idx,num in enumerate(nums):
            diff = target - num
            diff_indx[num].append(idx)
            if diff in diff_indx.keys() and diff_indx[diff][0] != idx:
                print(diff_indx[diff][0],idx)
                return [diff_indx[diff][0],idx]
