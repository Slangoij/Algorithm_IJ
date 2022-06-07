import Programmers.KakaoIntern2020.수식최대화;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        수식최대화 solu = new 수식최대화();

        String expression = "100-200*300-500+20";
        System.out.println(solu.solution(expression));
    }
}
