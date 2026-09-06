class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        max_len = 1
        left,right = 0,1
        char_map = {}
        if s[left] != s[right]:
            char_map[s[left]] = 1
            char_map[s[right]] = 1
            max_char = 1
        else:
            char_map[s[left]] = 2
            max_char = 2

        while right <= len(s) - 1:

            win_len = right - left + 1
            max_char = max(char_map.values(), default=0)
            
            required = win_len - max_char
            
            # print("max char: ",max_char)
            # print(left,right,required)
            if required <= k:
                if max_len < win_len:
                    max_len = win_len
                if right + 1 <= len(s) - 1:
                    right+=1
                    char_map[s[right]] = char_map.get(s[right], 0) + 1
                else:
                    break
            else:
                while required > k:
                    char_map[s[left]]-=1
                    left+=1
                    if left == right:
                        break
                    max_char = max(char_map.values(), default=0)
                    required = right - left + 1 - max_char


        return max_len
        