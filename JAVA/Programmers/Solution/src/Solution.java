import java.util.ArrayList;
import java.util.Collections;

public class Solution {
    public String solution(int n) {
        String answer = "";
        String numset = "124";
        int divided;
        String nowchar;
        while (n > 3) {
            divided = (n-1) % 3;
            nowchar = numset.substring(divided+1, divided+2);
            answer += nowchar;
            n = (int)((n-1)/ 3) + 1;
        }
        nowchar = numset.substring(n, n+1);
        answer += nowchar;

        StringBuffer sb = new StringBuffer(answer);

        return sb.reverse().toString();
    }

    public static void main(String[] args) {
        Solution tmp = new Solution();
        int n = 6;
        System.out.println(tmp.solution(n));
//        for (int i=1;i<20;i++) {
//            System.out.println(tmp.solution(i));
//        }
    }
}
