class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] result = new int[2];
        int left = 0, right = numbers.length - 1;

        while(left < right){

            int total = numbers[left] + numbers[right];

            if(total < target){
                int left_num = numbers[left];
                while(numbers[left] == left_num){
                    left++;
                }
            }else if(total > target){
                int right_num = numbers[right];
                while(right_num == numbers[right]){
                    right--;
                }
            }else{
                result[0] = left + 1;
                result[1] = right + 1;
                break;
                
            }
        }
        return result;
    }
}
