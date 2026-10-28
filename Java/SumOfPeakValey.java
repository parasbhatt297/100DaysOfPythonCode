import java.util.*;
public class SumOfPeakValey {
    public static int tsum(int[]nums){
        int ans = 0, n  = nums.length ;
        for(int i = 1 ; i<n-1 ; i++){
         if(nums[i]>nums[i-1] && nums[i]>nums[i+1] || nums[i]<nums[i-1]&&nums[i]<nums[i+1])ans+=nums[i];
        }
        return ans;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [] nums  = new int[n];
        for(int i = 0 ; i<n ; i++){
            nums[i] = sc.nextInt();
        }
        int ans = tsum(nums);
        System.out.println("The Sum of Peak and Valey is :" + ans);
        sc.close();
    }
}
