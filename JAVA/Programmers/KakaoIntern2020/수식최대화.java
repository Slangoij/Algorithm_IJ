package Programmers.KakaoIntern2020;

import java.sql.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class 수식최대화 {
    ArrayList<String> retList = new ArrayList<>();
    ArrayList<String> retOpList = new ArrayList<>();
    long gAnswer;

    public String calPrac(String a, String b, String op) {
        Long tmpa = Long.parseLong(a);
        Long tmpb = Long.parseLong(b);
        long ret;
        if (op.equals("*")) {
            ret = tmpa * tmpb;
        } else if (op.equals("-")) {
            ret = tmpa - tmpb;
        } else {
            ret = tmpa + tmpb;
        }
        return String.valueOf(ret);
    }
//    public boolean isNum(String str) {
//        for (int i = 0; i < str.length(); i++) {
//            if (!Character.isDigit(str.charAt(i))) {
//                return false;
//            }
//        }
//        return true;
//    }

    public void calByOp(ArrayList<String> splitstr,
                                     ArrayList<String> opers,
                                     String op) {

        for (int i = 0; i < opers.size(); i++) {
            if (opers.get(i).equals(op)) {
                retList.add(calPrac(splitstr.get(i), splitstr.get(i + 1), opers.get(i)));
            } else {
                retList.add(splitstr.get(i));
                retOpList.add(opers.get(i));
            }
        }
    }

    public void dfs(ArrayList<String> splitstr, ArrayList<String> opers) {
        String[] nowopers = {"*", "-", "+"};
        int k;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3 && j != i; j++) {
                retList.clear();
                retOpList.clear();
                k = 3 - i - j;
                calByOp(splitstr, opers, nowopers[i]);
                calByOp(splitstr, opers, nowopers[j]);
                calByOp(splitstr, opers, nowopers[k]);

                gAnswer = Math.max(gAnswer, Long.parseLong(retList.get(0)));
            }
        }

    }

    public long solution(String expression) {
        gAnswer = 0;

        ArrayList<String> splitstr =
                new ArrayList<>(Arrays.asList(expression.split("[*\\-+]")));

        ArrayList<String> opers = new ArrayList<>();
        for (int i = 0; i < expression.length(); i++) {
            char tmpchr = expression.charAt(i);
            if (!Character.isDigit(tmpchr)) {
                opers.add(Character.toString(tmpchr));
            }
        }

        dfs(splitstr, opers);

        return gAnswer;
    }
}
