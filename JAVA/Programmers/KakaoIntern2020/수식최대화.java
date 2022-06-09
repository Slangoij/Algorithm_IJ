package Programmers.KakaoIntern2020;

import java.sql.Array;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class 수식최대화 {
    ArrayList<Long> retList = new ArrayList<>();
    ArrayList<String> retOpList = new ArrayList<>();
    Set<String> operset = new HashSet<>();
    List<Long> splitstr = new ArrayList<>();
    ArrayList<String> opers = new ArrayList<>();
    long gAnswer;
    int[] permArr;

    static void swap(int[] arr, int depth, int i) {
        int temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
    }

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

    public void calByOp(String op) {
        ArrayList<Long> finRetList = new ArrayList<>();
        ArrayList<String> finRetOpList = new ArrayList<>();
        int cursor = 0;
        while (cursor < retList.size()-1) {
            Long aLong1 = retList.get(cursor);
            Long aLong2 = retList.get(cursor+1);
            String op1 = retOpList.get(cursor);
            if (op1.equals(op)) {
                retList.set(cursor, calPrac(aLong1, aLong2, op1));
                retOpList.set(cursor, op1);
                retList.remove(cursor);
            }
//            else {
//                retList.add(aLong1);
//                retOpList.add(op1);
//            }
            cursor++;
        }
    }

    public void permute(int now, int trg) {
        if (now == trg) {
            ArrayList<String> tmpoperlst = new ArrayList<>(operset);
            for (int i = 0; i < trg; i++) {
                calByOp(tmpoperlst.get(permArr[i]));
            }
            gAnswer = Math.max(gAnswer, retList.get(0));
            retList.clear();
            retOpList.clear();
        }
        for (int i = now; i < trg; i++) {
            swap(permArr, now, i);
            permute(now+1, trg);
            swap(permArr, now, i);
        }


//        int k;
//        for (int i = 0; i < 3; i++) {
//            for (int j = 0; j < 3 && j != i; j++) {
//                retList.clear();
//                retOpList.clear();
//                k = 3 - i - j;
//                calByOp(splitstr, opers, nowopers[i]);
//                calByOp(splitstr, opers, nowopers[j]);
//                calByOp(splitstr, opers, nowopers[k]);
//
//                gAnswer = Math.max(gAnswer, retList.get(0));
//            }
//        }

    }

    public long solution(String expression) {
        gAnswer = 0;

        List<String> splitstrarr = new ArrayList<>(Arrays.asList(expression.split("[*\\-+]")));
        for (String a : splitstrarr) {
            long l = Long.parseLong(a);
            retList.add(l);
            splitstr.add(l);
        }

        for (int i = 0; i < expression.length(); i++) {
            char tmpchr = expression.charAt(i);
            if (!Character.isDigit(tmpchr)) {
                String tmpstr = Character.toString(tmpchr);
                retOpList.add(tmpstr);
                operset.add(tmpstr);
                opers.add(tmpstr);
            }
        }

        permArr = new int[operset.size()];
        for (int i = 0; i < operset.size(); i++) {
            permArr[i] = i;
        }

        int a = operset.size();
        permute(0, operset.size());

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
