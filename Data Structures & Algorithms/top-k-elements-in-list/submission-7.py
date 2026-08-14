class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numfreq_map = {}
        for num in nums:
            numfreq_map[num] = numfreq_map.get(num,0) + 1
        # print(numfreq_map)

        freqnum_map = defaultdict(list)
        for key,value in numfreq_map.items():
            freqnum_map[value].append(key)
        print(freqnum_map)

        sorted_list = sorted(freqnum_map.keys(),reverse=True)
        print("Sorted: ",sorted_list)
        final_list = []
        for i in range(k):
            
            final_list.extend(freqnum_map[sorted_list[i]])
            print(f"i: {i}, length: {len(final_list)}")
            if len(final_list) >= k:
                break
        return final_list