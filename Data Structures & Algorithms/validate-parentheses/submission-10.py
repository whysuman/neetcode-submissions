class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {')': '(', '}': '{', ']': '['}
        result = []
        for char in s:
            if char in bracks.values():
                result.append(char)
            else:
                if len(result) != 0 and result[-1] == bracks[char]:
                    result.pop()
                else:
                    return False
        
        if len(result) == 0:
            return True
        else:
            return False

        