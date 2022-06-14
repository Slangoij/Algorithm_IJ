package Programmers;

import java.util.ArrayList;

public class 조이스틱 {
    public int getDistFromA(char chr) {
        int a = (int) 'Z' + 1;
        int b = (int)'A';
        return Math.min(Math.abs(a - (int) chr), Math.abs((int) chr - b));
    }

    public int solution(String name) {
        int answer = 0;
        int cnt = 0;
        int maxdist = 0;
        for (int i = 0; i < name.length(); i++) {
            answer += getDistFromA(name.charAt(i));
            if (name.charAt(i) != 'A' && i != 0) {
                cnt++;
                maxdist = Math.max(maxdist, Math.min(name.length() - i, i));
            }
        }
        return answer + Math.max(cnt, maxdist);
    }
}
