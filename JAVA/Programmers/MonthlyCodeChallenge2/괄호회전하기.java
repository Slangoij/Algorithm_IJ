package Programmers.MonthlyCodeChallenge2;

import java.util.ArrayList;

public class 괄호회전하기 {
    public boolean chkString(String s) {
        char[] chararr = s.toCharArray();
        ArrayList<Character> chrlst = new ArrayList<>();
        for (char c : chararr) {
            if (c == '[' || c == '{' || c == '(') {
                chrlst.add(c);
            } else if (chrlst.size() > 0) {
                Character lastchr = chrlst.get(chrlst.size() - 1);
                if ((lastchr == '[' && c == ']') ||
                        (lastchr == '{' && c == '}') ||
                        (lastchr == '(' && c == ')')) {
                    chrlst.remove(chrlst.size() - 1);
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        if (chrlst.size() > 0) return false;
        return true;
    }

    public String rotate(String s) {
        char firstchr = s.charAt(0);
        String newstr = new String(s + firstchr);
        return newstr.substring(1);
    }

    public int solution(String s) {
        int answer = 0;

        for (int i = 0; i < s.length(); i++) {
            if (chkString(s)) {
                answer++;
            }
            s = rotate(s);
        }

        return answer;
    }
}
