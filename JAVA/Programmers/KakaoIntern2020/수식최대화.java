package Programmers.KakaoIntern2020;

import java.sql.Array;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class 수식최대화 {
    ArrayList<Long> retList = new ArrayList<>();
    ArrayList<String> retOpList = new ArrayList<>();
    ArrayList<Long> splitstr = new ArrayList<>();
    ArrayList<String> opers = new ArrayList<>();
    Set<String> operset = new HashSet<>();
    ArrayList<String> tmpoperlst;
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
        int cursor = 0;
        while (cursor < retList.size()-1) {
            Long aLong1 = retList.get(cursor);
            Long aLong2 = retList.get(cursor+1);
            String op1 = retOpList.get(cursor);
            if (op1.equals(op)) {
                retList.set(cursor, calPrac(aLong1, aLong2, op1));
                retList.remove(cursor+1);
                retOpList.remove(cursor);
            }
//            else {
//                retList.add(aLong1);
//                retOpList.add(op1);
//            }
            else{
                cursor++;
            }
        }
    }

    public void permute(int now, int trg) {
        if (now == trg) {
            for (int i = 0; i < trg; i++) {
                calByOp(tmpoperlst.get(permArr[i]));
            }
            gAnswer = Math.max(gAnswer, Math.abs(retList.get(0)));
            retList = new ArrayList<>();
            retOpList = new ArrayList<>();
            retList.addAll(splitstr);
            retOpList.addAll(opers);
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

        List<String> tmpSplitStrArr = new ArrayList<>(Arrays.asList(expression.split("[*\\-+]")));
        for (String a : tmpSplitStrArr) {
            long l = Long.parseLong(a);
            splitstr.add(l);
        }

        for (int i = 0; i < expression.length(); i++) {
            char tmpchr = expression.charAt(i);
            if (!Character.isDigit(tmpchr)) {
                String tmpstr = Character.toString(tmpchr);
                operset.add(tmpstr);
                opers.add(tmpstr);
            }
        }

        tmpoperlst = new ArrayList<>(operset);
        permArr = new int[operset.size()];
        for (int i = 0; i < operset.size(); i++) {
            permArr[i] = i;
        }

        retList = new ArrayList<>();
        retOpList = new ArrayList<>();
        retList.addAll(splitstr);
        retOpList.addAll(opers);
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
