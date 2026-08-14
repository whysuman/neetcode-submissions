class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = [[] for i in range(len(nums))]
        num_freq = {}
        for indx,num in enumerate(nums):
            if num in num_freq.keys():
                num_freq[num]+=1
            else:
                num_freq[num] = 1
        
        # print(num_freq)
        for key,value in num_freq.items():
            # print(value)
            freq_map[value - 1].append(key)
        
        result = []
        for item in reversed(freq_map):
            for val in item:
                k-=1
                result.append(val)
                if k <= 0:
                    return result


        