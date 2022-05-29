package Programmers.Kakaocode2017;

import java.util.*;
public class 단체사진찍기 {
    int answer = 0;
    Map<String, Integer> posMap = new HashMap<String, Integer>();
    boolean[] vstd = new boolean[8];
    String[] tmpdata;

    static int facto(int n) {
        if (n > 0) {
            return n * facto(n - 1);
        }
        return 1;
    }

    public void dfs(int now, int n) {
        if (now == n) {
            int tmpcnt = 0;
            for (int i = 0; i < 8; i++) {
                if (!vstd[i]) {
                    tmpcnt++;
                }
            }
            answer += facto(tmpcnt);
            return;
        }
        String data = tmpdata[now];
        String fr1 = data.substring(0,1);
        String fr2 = data.substring(1,2);
        int dist = data.charAt(2) - '0' + 1;
        char compar = data.charAt(3);
        Integer nowpos1 = posMap.get(fr1);
        Integer nowpos2 = posMap.get(fr2);
        if (nowpos1 < 0 && nowpos2 < 0) {
            for (int i = 0; i < 8; i++) {
                if (!vstd[i]) {
                    vstd[i] = true;
                    posMap.put(fr1, i);
                    if (compar == '<') {
                        for (int j = 1; j < dist; j++) {
                            if (0 <= i + j && i + j < 8 && !vstd[i + j]) {
                                vstd[i + j] = true;
                                posMap.put(fr2, i + j);
                                dfs(now + 1, n);
                                vstd[i + j] = false;
                                posMap.put(fr2, -1);
                            }
                            if (0 <= i - j && i - j < 8 && !vstd[i - j]) {
                                vstd[i - j] = true;
                                posMap.put(fr2, i - j);
                                dfs(now + 1, n);
                                vstd[i - j] = false;
                                posMap.put(fr2, -1);
                            }
                        }
                    }
                    else if (compar == '>') {
                        for (int j = dist+1; j <= 7; j++) {
                            if (0 <= i + j && i + j < 8 && !vstd[i + j]) {
                                vstd[i + j] = true;
                                posMap.put(fr2, i + j);
                                dfs(now + 1, n);
                                vstd[i + j] = false;
                                posMap.put(fr2, -1);
                            }
                            if (0 <= i - j && i - j < 8 && !vstd[i - j]) {
                                vstd[i - j] = true;
                                posMap.put(fr2, i - j);
                                dfs(now + 1, n);
                                vstd[i - j] = false;
                                posMap.put(fr2, -1);
                            }
                        }
                    }
                    else {
                        if (0 <= i + dist && i + dist < 8 && !vstd[i + dist]) {
                            vstd[i + dist] = true;
                            posMap.put(fr2, i + dist);
                            dfs(now + 1, n);
                            vstd[i + dist] = false;
                            posMap.put(fr2, -1);
                        }
                        if (0 <= i - dist && i - dist < 8 && !vstd[i - dist]) {
                            vstd[i - dist] = true;
                            posMap.put(fr2, i - dist);
                            dfs(now + 1, n);
                            vstd[i - dist] = false;
                            posMap.put(fr2, -1);
                        }
                    }
                    vstd[i] = false;
                    posMap.put(fr1, -1);
                }
            }
        }
        else if (nowpos1 >= 0 && nowpos2 >= 0) {
            if ((compar == '<' && Math.abs(nowpos1 - nowpos2) < dist)||
                    (compar == '>' && Math.abs(nowpos1 - nowpos2) > dist)||
                    (compar == '=' && Math.abs(nowpos1 - nowpos2) == dist)) {
                dfs(now + 1, n);
            }
            else{
                return;
            }
        }
        else {
            Integer nowpos = (nowpos1 < 0) ? nowpos1 : nowpos2;
            String fr = (posMap.get(fr1) < 0) ? fr1 : fr2;
            if (compar == '<') {
                for (int i = 1; i < dist; i++) {
                    if (0 <= nowpos + i && nowpos + i < 8 && !vstd[nowpos + i]) {
                        vstd[nowpos + i] = true;
                        posMap.put(fr, nowpos + i);
                        dfs(now + 1, n);
                        vstd[nowpos + i] = false;
                        posMap.put(fr, -1);
                    }
                    if (0 <= nowpos - i && nowpos - i < 8 && !vstd[nowpos - i]) {
                        vstd[nowpos - i] = true;
                        posMap.put(fr, nowpos - i);
                        dfs(now + 1, n);
                        vstd[nowpos - i] = false;
                        posMap.put(fr, -1);
                    }
                }
            }
            else if (compar == '>') {
                for (int j = dist + 1; j <= 7; j++) {
                    if (0 <= nowpos + j && nowpos + j < 8 && !vstd[nowpos + j]) {
                        vstd[nowpos + j] = true;
                        posMap.put(fr, nowpos + j);
                        dfs(now + 1, n);
                        vstd[nowpos + j] = false;
                        posMap.put(fr, -1);
                    }
                    if (0 <= nowpos - j && nowpos - j < 8 && !vstd[nowpos - j]) {
                        vstd[nowpos - j] = true;
                        posMap.put(fr, nowpos - j);
                        dfs(now + 1, n);
                        vstd[nowpos - j] = false;
                        posMap.put(fr, -1);
                    }
                }
            }
            else {
                if (0 <= nowpos + dist && nowpos + dist < 8 && !vstd[nowpos + dist]) {
                    vstd[nowpos + dist] = true;
                    posMap.put(fr, nowpos + dist);
                    dfs(now + 1, n);
                    vstd[nowpos + dist] = false;
                    posMap.put(fr, -1);
                }
                if (0 <= nowpos - dist && nowpos - dist < 8 && !vstd[nowpos - dist]) {
                    vstd[nowpos - dist] = true;
                    posMap.put(fr, nowpos - dist);
                    dfs(now + 1, n);
                    vstd[nowpos - dist] = false;
                    posMap.put(fr, -1);
                }
            }
        }
    }

    public int solution(int n, String[] data) {
        for (int i = 0; i < 8; i++) {
            vstd[i] = false;
        }
        String a = "ACFJMNRT";
        for (int i = 0; i < 8; i++) {
            posMap.put(a.substring(i, i + 1), -1);
        }
        tmpdata = new String[data.length];
        int idx = 0;
        for (String str : data) {
            char[] tmpchr = str.toCharArray();
            Arrays.sort(tmpchr);
            char[] tmptmpchr = {tmpchr[2], tmpchr[3], tmpchr[0], tmpchr[1]};
            tmpdata[idx++] = new String(tmptmpchr);
        }
        Arrays.sort(tmpdata);

        dfs(0, n);

        return answer;
    }
}
// 첫번째 시도: 효율성부터 생각해서 각 프렌즈의 위치만 저장하고 되는 친구들부터 껴넣고 판단.
//
//public class 단체사진찍기 {
//    int answer = 0;
//    Map<String, Integer> posMap = new HashMap<String, Integer>();
//    boolean[] vstd = new boolean[8];
//    String[] tmpdata;
//
//    static int facto(int n) {
//        if (n > 0) {
//            return n * facto(n - 1);
//        }
//        return 1;
//    }
//
//    public void dfs(int now, int n) {
//        if (now == n) {
//            int tmpcnt = 0;
//            for (int i = 0; i < 8; i++) {
//                if (!vstd[i]) {
//                    tmpcnt++;
//                }
//            }
//            answer += facto(tmpcnt);
//            return;
//        }
//        String data = tmpdata[now];
//        String fr1 = data.substring(0,1);
//        String fr2 = data.substring(1,2);
//        int dist = data.charAt(2) - '0' + 1;
//        char compar = data.charAt(3);
//        Integer nowpos1 = posMap.get(fr1);
//        Integer nowpos2 = posMap.get(fr2);
//        if (nowpos1 < 0 && nowpos2 < 0) {
//            for (int i = 0; i < 8; i++) {
//                if (!vstd[i]) {
//                    vstd[i] = true;
//                    posMap.put(fr1, i);
//                    if (compar == '<') {
//                        for (int j = 1; j < dist; j++) {
//                            if (0 <= i + j && i + j < 8 && !vstd[i + j]) {
//                                vstd[i + j] = true;
//                                posMap.put(fr2, i + j);
//                                dfs(now + 1, n);
//                                vstd[i + j] = false;
//                                posMap.put(fr2, -1);
//                            }
//                            if (0 <= i - j && i - j < 8 && !vstd[i - j]) {
//                                vstd[i - j] = true;
//                                posMap.put(fr2, i - j);
//                                dfs(now + 1, n);
//                                vstd[i - j] = false;
//                                posMap.put(fr2, -1);
//                            }
//                        }
//                    }
//                    else if (compar == '>') {
//                        for (int j = dist+1; j <= 7; j++) {
//                            if (0 <= i + j && i + j < 8 && !vstd[i + j]) {
//                                vstd[i + j] = true;
//                                posMap.put(fr2, i + j);
//                                dfs(now + 1, n);
//                                vstd[i + j] = false;
//                                posMap.put(fr2, -1);
//                            }
//                            if (0 <= i - j && i - j < 8 && !vstd[i - j]) {
//                                vstd[i - j] = true;
//                                posMap.put(fr2, i - j);
//                                dfs(now + 1, n);
//                                vstd[i - j] = false;
//                                posMap.put(fr2, -1);
//                            }
//                        }
//                    }
//                    else {
//                        if (0 <= i + dist && i + dist < 8 && !vstd[i + dist]) {
//                            vstd[i + dist] = true;
//                            posMap.put(fr2, i + dist);
//                            dfs(now + 1, n);
//                            vstd[i + dist] = false;
//                            posMap.put(fr2, -1);
//                        }
//                        if (0 <= i - dist && i - dist < 8 && !vstd[i - dist]) {
//                            vstd[i - dist] = true;
//                            posMap.put(fr2, i - dist);
//                            dfs(now + 1, n);
//                            vstd[i - dist] = false;
//                            posMap.put(fr2, -1);
//                        }
//                    }
//                    vstd[i] = false;
//                    posMap.put(fr1, -1);
//                }
//            }
//        }
//        else if (nowpos1 >= 0 && nowpos2 >= 0) {
//            if ((compar == '<' && Math.abs(nowpos1 - nowpos2) < dist)||
//                    (compar == '>' && Math.abs(nowpos1 - nowpos2) > dist)||
//                    (compar == '=' && Math.abs(nowpos1 - nowpos2) == dist)) {
//                dfs(now + 1, n);
//            }
//            else{
//                return;
//            }
//        }
//        else {
//            Integer nowpos = (nowpos1 < 0) ? nowpos1 : nowpos2;
//            String fr = (posMap.get(fr1) < 0) ? fr1 : fr2;
//            if (compar == '<') {
//                for (int i = 1; i < dist; i++) {
//                    if (0 <= nowpos + i && nowpos + i < 8 && !vstd[nowpos + i]) {
//                        vstd[nowpos + i] = true;
//                        posMap.put(fr, nowpos + i);
//                        dfs(now + 1, n);
//                        vstd[nowpos + i] = false;
//                        posMap.put(fr, -1);
//                    }
//                    if (0 <= nowpos - i && nowpos - i < 8 && !vstd[nowpos - i]) {
//                        vstd[nowpos - i] = true;
//                        posMap.put(fr, nowpos - i);
//                        dfs(now + 1, n);
//                        vstd[nowpos - i] = false;
//                        posMap.put(fr, -1);
//                    }
//                }
//            }
//            else if (compar == '>') {
//                for (int j = dist + 1; j <= 7; j++) {
//                    if (0 <= nowpos + j && nowpos + j < 8 && !vstd[nowpos + j]) {
//                        vstd[nowpos + j] = true;
//                        posMap.put(fr, nowpos + j);
//                        dfs(now + 1, n);
//                        vstd[nowpos + j] = false;
//                        posMap.put(fr, -1);
//                    }
//                    if (0 <= nowpos - j && nowpos - j < 8 && !vstd[nowpos - j]) {
//                        vstd[nowpos - j] = true;
//                        posMap.put(fr, nowpos - j);
//                        dfs(now + 1, n);
//                        vstd[nowpos - j] = false;
//                        posMap.put(fr, -1);
//                    }
//                }
//            }
//            else {
//                if (0 <= nowpos + dist && nowpos + dist < 8 && !vstd[nowpos + dist]) {
//                    vstd[nowpos + dist] = true;
//                    posMap.put(fr, nowpos + dist);
//                    dfs(now + 1, n);
//                    vstd[nowpos + dist] = false;
//                    posMap.put(fr, -1);
//                }
//                if (0 <= nowpos - dist && nowpos - dist < 8 && !vstd[nowpos - dist]) {
//                    vstd[nowpos - dist] = true;
//                    posMap.put(fr, nowpos - dist);
//                    dfs(now + 1, n);
//                    vstd[nowpos - dist] = false;
//                    posMap.put(fr, -1);
//                }
//            }
//        }
//    }
//
//    public int solution(int n, String[] data) {
//        for (int i = 0; i < 8; i++) {
//            vstd[i] = false;
//        }
//        String a = "ACFJMNRT";
//        for (int i = 0; i < 8; i++) {
//            posMap.put(a.substring(i, i + 1), -1);
//        }
//        tmpdata = new String[data.length];
//        int idx = 0;
//        for (String str : data) {
//            char[] tmpchr = str.toCharArray();
//            Arrays.sort(tmpchr);
//            char[] tmptmpchr = {tmpchr[2], tmpchr[3], tmpchr[0], tmpchr[1]};
//            tmpdata[idx++] = new String(tmptmpchr);
//        }
//        Arrays.sort(tmpdata);
//
//        dfs(0, n);
//
//        return answer;
//    }
//}
