class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #MAIN CONSTRAINT -- HAS EXACTLY ONE PAIR OF INPUT THAT SATISFIES OF THE TARGET SUM
        #CONSIDER INPUT = [0,-1,5,7] target = -1
        indx_map = {}
        for indx,num in enumerate(nums):
            indx_map[num] = indx 

        for indx,num in enumerate(nums):
            complimentary_num = target - num
            print(num,complimentary_num)
            if complimentary_num in indx_map and indx != indx_map[complimentary_num
            ]:
                if  indx > indx_map[complimentary_num]:
                    return [indx_map[complimentary_num],indx]
                else:
                    return[indx,indx_map[complimentary_num]]
