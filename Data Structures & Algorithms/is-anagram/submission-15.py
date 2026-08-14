class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_freq = [0] * 26
        if len(s) != len(t):
            return False
        length = len(s)
        for i in range(length):
            char_freq[ord(s[i]) - ord('a')]+=1
            char_freq[ord(t[i]) - ord('a')]-=1


        return all(v == 0 for v in char_freq)
            
        
        
        