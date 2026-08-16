class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #I need to get all possible consecutive sequences
        if nums == []:
            return 0
        
        result = set()
        print(nums)
        for ind,val in enumerate(nums):
            result.add(val)

        start_indx = []
        for num in nums:
            if num - 1 not in result:
                start_indx.append(num)

        count = 1
        for indx in start_indx:
            num = indx
            temp_count = 1
            while True:
                if num + 1 in result:
                    temp_count+=1
                    num+=1
                else:
                    if temp_count > count:
                        count = temp_count
                    break

        return count
                


        

        print(result)
        print(start_indx)

        return 1

