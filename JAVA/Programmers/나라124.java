package Programmers;

public class 나라124 {
    public String solution(int n) {
        String answer = "";
        String numset = "124";
        int divided;
        String nowchar;
        while (n > 3) {
            divided = (n+2) % 3;
            nowchar = numset.substring(divided, divided+1);
            answer += nowchar;
            n = (int)((n-1)/ 3);
        }
        nowchar = numset.substring(n-1, n);
        answer += nowchar;

        StringBuffer sb = new StringBuffer(answer);

        return sb.reverse().toString();
    }
}
