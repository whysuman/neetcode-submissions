class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = defaultdict(list)
        for i,value in enumerate(nums):
            hashtable[value].append(i)
            # print(hashtable[value])
        for value in hashtable.values():
            # print(len(value))
            if len(value) > 1:
                return True
        return False