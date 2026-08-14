class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i,ix in enumerate(nums):
            for j, jx in enumerate(nums):
                if i != j:
                    print(i,j,ix,jx)
                    if ix == jx:
                        return True
        return False
         