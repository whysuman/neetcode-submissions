class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq_list = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num,0) + 1
        for key,value in count.items():
            freq_list[value].append(key)

        res = []
        for i in range(len(freq_list) - 1,0,-1):
            for num in freq_list[i]:
                res.append(num)
            if len(res) == k:
                return res
