class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left, right = 0,0
        max_ct = 0
        curr = 0

        while right <= len(s) - 1:
        
            if s[right] in char_map:
                if max_ct < curr:
                    max_ct = curr
                left = max(left,char_map[s[right]] + 1)   
                    
            curr = right - left + 1
            char_map[s[right]] = right
            right+=1
            # print(char_map)

        return max(curr,max_ct)
            

        