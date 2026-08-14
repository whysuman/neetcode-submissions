class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Creating a mapping from number to its frequency using a dictionary
        numfreq_map = {}
        for num in nums:
            numfreq_map[num] = numfreq_map.get(num,0) + 1
        
        #Now creating a frequency buckets using list of lists, where each sub list is a frequency bucket
        #Each frequency bucket will have the numbers that are repeating with that respective frequency
        freqnum_map = [[] for _ in range(max(numfreq_map.values()) + 1)]
        for key,value in numfreq_map.items():
            freqnum_map[value].append(key)
        

        final_list = []
        for item in reversed(freqnum_map): #Going throught the frequency buckets in descending order
            #We are going to add a bucket's values and check if the final list length is greater than the k
            final_list.extend(item) 
            if len(final_list) >= k:
                break
        return final_list