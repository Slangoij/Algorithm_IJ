import Programmers.DevMatching2021WebBackend.다단계칫솔판매;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        다단계칫솔판매 solu = new 다단계칫솔판매();

        String[] enroll = {"john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"};
        String[] referral = {"-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"};
        String[] seller = {"young", "john", "tod", "emily", "mary"};
        int[] amount = {12, 4, 2, 5, 10};

        System.out.println(Arrays.toString(solu.solution(
                enroll, referral, seller, amount
        )));
    }
}
