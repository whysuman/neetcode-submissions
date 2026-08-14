class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test_dict = {}
        for ind,ele in enumerate(nums):
            print(f"{ele} : {ind}")
            if ele not in test_dict:
                test_dict[ele] = ind
            else:
                return True
        return False



