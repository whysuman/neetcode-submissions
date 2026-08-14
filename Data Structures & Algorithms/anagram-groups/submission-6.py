class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = defaultdict(list)

        for string in strs:
            curr_map = [0]*26
            for char in string:
                curr_map[ord(char) - ord('a')]+=1
            char_map[tuple(curr_map)].append(string)
        
        result = []
        for key,value in char_map.items():
            result.append(value)

        return result
        