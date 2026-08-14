class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp_result = set()
        for i in range(len(nums)):
            temp_result.add(nums[i])
        
        start_pos = []
        for item in temp_result:
            if item - 1 not in temp_result:
                start_pos.append(item)

        max_len = 0
        for start in start_pos:
            count = 1
            while True:
                if start + 1 in temp_result:
                    count+=1
                    start+=1
                else:
                    break
            if count > max_len:
                max_len = count

        return max_len
            