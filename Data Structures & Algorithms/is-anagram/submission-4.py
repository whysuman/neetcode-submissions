class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = [0]*26
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        for char in t:
            char_count[ord(char) - ord('a')] -=1
        
        if char_count == [0]*26:
            return True
        else:
            return False