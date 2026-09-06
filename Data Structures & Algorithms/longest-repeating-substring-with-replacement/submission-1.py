class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
          char_map = {}
          left = 0
          max_freq = 0
          max_length = 0
          for right in range(len(s)):
              char_map[s[right]] = char_map.get(s[right], 0) + 1
              max_freq = max(max_freq, char_map[s[right]])
              if (right - left + 1) - max_freq > k:
                  char_map[s[left]] -= 1
                  left += 1
              max_length = max(max_length, right - left + 1)
          return max_length
        