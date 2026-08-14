class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set()
        if len(nums) == 0:
            return 0
        for idx,num in enumerate(nums):
            hashmap.add(num)
        
        strt = set()
        for num in nums:
            if num-1 not in hashmap:
                strt.add(num)
        
        print(hashmap)
        max_len = 1
        print(strt)
        for num in strt:
            print(num)
            count = 1
            while True:
                if num + 1 in hashmap:
                    count+=1
                    num+=1
                    
                if num + 1 not in hashmap:
                    break

            if count > max_len:
                max_len = count

        return max_len
             