package Programmers.SummerWinterCodingBefore2018;

import java.util.Arrays;

public class 소수만들기 {
    public int solution(int[] nums) {
        int answer = 0;
        Arrays.sort(nums);
        int numleng = nums.length;
        int maxsosu = nums[numleng - 1] + nums[numleng - 2] + nums[numleng - 3];

        boolean[] arr = new boolean[maxsosu + 1];
        Arrays.fill(arr, true);
        arr[0] = arr[1] = false;

        for (int i=2;i*i<=maxsosu;i++){
            if (arr[i]){
                for (int j=i*i;j<=maxsosu;j+=i){
                    arr[j] = false;
                }
            }
        }

        int tmpsum = 0;
        for (int i=0;i<nums.length;i++){
            for (int j=i+1;j<nums.length;j++){
                for (int k=j+1;k<nums.length;k++){
                    tmpsum = nums[i] + nums[j] + nums[k];
                    if (arr[tmpsum]) answer += 1;
                }
            }
        }
        return answer;
    }
}
