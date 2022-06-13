package Programmers;

import java.util.*;

public class 짝지어제거하기 {
    public int solution(String s)
    {
        ArrayList<String> stack = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            String tmpchr = Character.toString(s.charAt(i));
            if (stack.size() > 0 && stack.get(stack.size() - 1).equals(tmpchr)) {
                stack.remove(stack.size() - 1);
            } else {
                stack.add(tmpchr);
            }
        }

        if (stack.isEmpty()) {
            return 1;
        }
        return 0;
    }
}
