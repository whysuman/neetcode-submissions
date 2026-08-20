class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights[0],heights[1])
        left, right = 0, len(heights) - 1
        max_area = -1
        while left < right:
            curr_area = min(heights[left],heights[right])*(right - left)
            if max_area < curr_area:
                max_area = curr_area
            
            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1

        return max_area
