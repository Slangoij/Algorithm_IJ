package Programmers.KakaoIntern2020;

import java.sql.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class 수식최대화 {
    ArrayList<Long> retList = new ArrayList<>();
    ArrayList<String> retOpList = new ArrayList<>();
    long gAnswer;

    public Long calPrac(Long a, Long b, String op) {
        long ret;
        if (op.equals("*")) {
            ret = a * b;
        } else if (op.equals("-")) {
            ret = a - b;
        } else {
            ret = a + b;
        }
        return ret;
    }

    public void calByOp(List<Long> splitstr,
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

    public void dfs(List<Long> splitstr, ArrayList<String> opers) {
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

                gAnswer = Math.max(gAnswer, retList.get(0));
            }
        }

    }

    public long solution(String expression) {
        gAnswer = 0;

        List<String> splitstrarr = new ArrayList<>(Arrays.asList(expression.split("[*\\-+]")));
        List<Long> splitstr = new ArrayList<>();
        for (String a : splitstrarr) {
            splitstr.add(Long.parseLong(a));
        }

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

//    public boolean isNum(String str) {
//        for (int i = 0; i < str.length(); i++) {
//            if (!Character.isDigit(str.charAt(i))) {
//                return false;
//            }
//        }
//        return true;
//    }
}
