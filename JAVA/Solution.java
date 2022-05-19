import Programmers.DevMatching2021WebBackend.다단계칫솔판매;
import Programmers.Kakao2019Blind.실패율;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        실패율 solu = new 실패율();

        int N = 3;
//        int[] stages = {2, 1, 2, 6, 2, 4, 3, 3};
        int[] stages = {1,1,1};

        System.out.println(Arrays.toString(solu.solution(
                N, stages
        )));
    }
}
