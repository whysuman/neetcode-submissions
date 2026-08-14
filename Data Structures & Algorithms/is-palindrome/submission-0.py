class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        
        result = ''.join(ch for ch in s if ch.isalnum())
        result = result.lower()
        print(result) 

        for i in range(len(result)):
            if result[i] != result[len(result) - i - 1]:                return False

        return True
        
        