class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0, len(numbers) - 1
        
        while left <= right:
            left_num = numbers[left]
            right_num = numbers[right]
            total = left_num + right_num
            print(left_num,right_num)

            if total == target:
                return [left + 1,right + 1]
            
            elif total < target:
                while numbers[left] == left_num:
                    left+=1
            else:
                while numbers[right] == right_num:
                    right-=1
        