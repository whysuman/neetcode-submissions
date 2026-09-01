class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = set()
        left, right = 0,0
        max_ct = 0
        curr = 0

        while right <= len(s) - 1:
        
            if s[right] in char_map:
                if max_ct < curr:
                    max_ct = curr
            
                while s[right] in char_map:
                    char_map.remove(s[left])
                    left+=1    
                    
            curr = right - left + 1
            char_map.add(s[right])
            right+=1
            # print(char_map)

        return max(curr,max_ct)
            

        