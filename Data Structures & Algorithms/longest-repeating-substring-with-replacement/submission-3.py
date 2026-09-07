class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Example : "AAABABB"
        char_map = {}
        left = 0
        max_len = 0
        max_freq = 0

        for right in range(len(s)):
            char_map[s[right]] = char_map.get(s[right],0) + 1
            max_freq = max(char_map[s[right]],max_freq)
            req_changes = right - left + 1 - max_freq

            if req_changes > k:
                char_map[s[left]]-=1
                left+=1

        max_len = max(max_len,right - left + 1) #Safe to always update. If we just shrank, since both the right and left the window length will remain the same to the preshrik win len, meaning the max_len will not change.(As it also greater than or equal to the preshrink length)

        return max_len
        