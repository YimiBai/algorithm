package code;
/* Some of the numbers from 1 to N in stored in nums[1..N],
count the frequency of every number without using extra space
For example: nums = {2,1,1,2,2,4}, result = {2,3,0,1,0,0}, for '1' appears 2 times, '2' appears 3 times and '4' appears 1 time
*/
public class code {
    public static void main(String[] args){
        int[] nums = {2,1,1,2,2,4};
        int temp;
        for (int i=0;i<nums.length;i++){
            while (nums[i]>0){
                if (nums[i]-1 == i)
                    nums[i] = -1;
                else if (nums[nums[i]-1]<=0)
                {nums[nums[i]-1] -= 1;nums[i]=0;}
                else{
                    temp = nums[i];
                    nums[i] = nums[nums[i]-1];
                    nums[temp-1] = -1;
                }
            }
        }
        for (int n:nums) System.out.println(-n);
    }
}
