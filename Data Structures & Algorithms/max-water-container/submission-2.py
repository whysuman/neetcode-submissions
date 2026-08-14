class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        #Dont forget to treat the edge case of len == 2
        # if len(heights) == 2:
        #     return min(heights[0],heights[1])

        left,right = 0, len(heights) - 1
        max_amt = 0
        while left < right:
            print(max_amt)
            
            if heights[left] > heights[right]:
                curr_max = heights[right]*(right-left)
                if curr_max > max_amt:
                    max_amt = curr_max
                right-=1
                
            elif heights[right] > heights[left]:
                curr_max = heights[left]*(right-left)
                if curr_max > max_amt:
                    max_amt = curr_max
                left+=1
            else:
                curr_max = heights[right]*(right-left)
                if curr_max > max_amt:
                    max_amt = curr_max
                left+=1
            print(curr_max)
        return max_amt