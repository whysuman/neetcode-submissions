class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        temp_result = set()
        # the following loop is O(n)
        for i in range(len(nums)):
            temp_result.add(nums[i])
        
        start_pos = []
        #Time complexity is O(n) again for the start pos check
        for item in temp_result:
            if item - 1 not in temp_result:
                start_pos.append(item)

        max_len = 0
        #The following is O(n) complexity as we only access unique elements for each start
        for start in start_pos:
            count = 1
            while start + 1 in temp_result:
                count+=1
                start+=1
            if count > max_len:
                max_len = count

        return max_len
            