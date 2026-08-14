class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_freq = defaultdict(list)
        for string in strs:
            char_freq = [0]*26
            for indx,char in enumerate(string):
                char_freq[ord(char) - ord('a')]+=1
            map_freq[tuple(char_freq)].append(string)
        
        result = []
        for value in map_freq.values():
            result.append(value)

        return result
            
            

        