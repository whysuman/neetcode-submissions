class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charcount = [0]*26

        for indx, schar in enumerate(s):
            charcount[ord(schar) - ord('a')]+=1
            charcount[ord(t[indx]) - ord('a')]-=1

        if charcount == [0]*26:
            return True
        else:
            return False

