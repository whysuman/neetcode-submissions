class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Example : "AAABABB"
          char_map = {}
          left = 0
          max_freq = 0
          max_length = 0
          for right in range(len(s)): # We are increasing the right pointer one by one
              char_map[s[right]] = char_map.get(s[right], 0) + 1 #Updating the char frequency of right pointer
              max_freq = max(max_freq, char_map[s[right]]) #
              req_changes = (right - left + 1) - max_freq
              if (right - left + 1) - max_freq > k: #(right - left + 1) - max_freq --> Shows number of characters to be changed for a contiguous sequence of one distice character
                  char_map[s[left]] -= 1
                  left += 1
              max_length = max(max_length, right - left + 1)
          return max_length
        