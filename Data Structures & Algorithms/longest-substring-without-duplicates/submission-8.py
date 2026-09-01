class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left, right = 0,0
        max_ct = 0

        while right <= len(s) - 1:
        
            if s[right] in char_map:
                left = max(left,char_map[s[right]] + 1) #It is important to move the left pointer to the max of left and s[right]'s last occurrence 
                    
            char_map[s[right]] = right
            curr = right - left + 1
            max_ct = max(max_ct,curr)
            right+=1
            # print(char_map)

        return max_ct
            

        