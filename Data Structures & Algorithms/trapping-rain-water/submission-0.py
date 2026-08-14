class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 2:
            return 0
        
        left_max = [0]
        maxl = height[0]
        right_max = [0]
        maxr = height[-1]

        for indx,val in enumerate(height):
            if indx == 0:
                continue
            # print(maxl)
            left_max.append(maxl)
            if maxl < val:
                maxl = val

        for indx,val in enumerate(reversed(height)):
            if indx == 0:
                continue
            
            right_max.append(maxr)
            if maxr < val:
                maxr = val

        right_max = list(reversed(right_max))
        # print(left_max,right_max)
        capacity = 0
        for indx,val in enumerate(height):
            if indx == 0 or indx == len(height) - 1:
                continue
            curr_capacity = min(left_max[indx],right_max[indx]) - val
            # print(f"Current capacity at index: {indx} is: {curr_capacity}")
            capacity += max(curr_capacity,0)
            # print(f"Water capacity: {capacity}")
        return capacity
            

            
            
            


            
