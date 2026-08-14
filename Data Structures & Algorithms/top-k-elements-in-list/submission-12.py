class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}

        #first calculate elemn -> count
        for num in nums:
            if num not in num_freq:
                num_freq[num] = 1
            else:
                num_freq[num] += 1
        
        freq_sort = [[] for _ in range(10000)]
        #then count -> [elems]
        for key,value in num_freq.items():
            freq_sort[value].append(key)

        result = []
        
        for val in reversed(freq_sort):
            if val != []:
                print(val,k)
                result.extend(val)
                k -= len(val)
                if k <= 0:
                    break
        return result
