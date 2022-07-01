import Programmers.위장;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        위장 solu = new 위장();

        String[][] s = {
                {"yellow_hat", "headgear"},
                {"blue_sunglasses", "eyewear"},
                {"green_turban", "headgear"}
        };
        System.out.println(solu.solution(s));
    }
}
