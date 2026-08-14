class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqtonum = [[] for _ in range(len(nums))]
        freqmap = {}

        for number in nums:
            if number in freqmap:
                freqmap[number]+=1
            else:
                freqmap[number] = 0

        for num,freq in freqmap.items():
            freqtonum[freq].append(num)

        final_res = []
        for i in range(len(freqtonum) - 1,-1,-1):
            if freqtonum[i] != []:
                k-= len(freqtonum[i])
                final_res.extend(freqtonum[i])
                print(f"k:{k} number: {freqtonum[i]}")
            if k == 0:
                break

        print(freqtonum,final_res)
        return final_res
            


