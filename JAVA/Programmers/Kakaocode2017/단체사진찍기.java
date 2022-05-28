package Programmers.Kakaocode2017;

import java.util.*;

public class 단체사진찍기 {
    int answer = 0;
    Map<String, Integer> posMap = new HashMap<String, Integer>();
    boolean[] vstd = new boolean[8];
    String[] tmpdata;
    int mint = Integer.MIN_VALUE;

    public void dfs(int now, int n) {
        if (now == n) {
            return;
        }
        String data = tmpdata[now];
        char fr1 = data.charAt(0);
        char fr2 = data.charAt(1);
        char compar = data.charAt(2);
        int dist = data.charAt(3) - '0';
        Integer nowpos1 = posMap.get(fr1);
        Integer nowpos2 = posMap.get(fr2);
        if (nowpos1 == mint) {
            for (int i = 0; i < 8; i++) {
                if (!vstd[i]) {
                    vstd[i] = true;

                    if (compar == '<') {
                        for (int j = 1; j < dist; j++) {
                            posMap.put(Character.toString(fr2),  + j);
                            dfs(now + 1, n);
                            posMap.put(Character.toString(fr2), posMap.get(fr1) - j*2);
                            dfs(now + 1, n);
                        }
                    } else if (compar == '>') {
                        for (int j = dist+1; j <= 7; j++) {
                            posMap.put(Character.toString(fr2), posMap.get(fr1) + j);
                            dfs(now + 1, n);
                            posMap.put(Character.toString(fr2), posMap.get(fr1) - j*2);
                            dfs(now + 1, n);
                        }
                    } else {
                        posMap.put(Character.toString(fr2), posMap.get(fr1) + dist);
                        dfs(now + 1, n);
                        posMap.put(Character.toString(fr2), posMap.get(fr1) - dist*2);
                        dfs(now + 1, n);
                    }

                    vstd[i] = false;
                }
                else{
                    break;
                }
            }
        }
    }

    public int solution(int n, String[] data) {
        for (int i = 0; i < 8; i++) {
            vstd[i] = false;
        }
        String a = "ACFJMNRT";
        for (char chr : a.toCharArray()) {
            posMap.put(Character.toString(chr), Integer.MIN_VALUE);
        }
        tmpdata = new String[data.length];
        int idx = 0;
        for (String str : data) {
            char[] tmpchr = str.toCharArray();
            Arrays.sort(tmpchr);
            char[] tmptmpchr = {tmpchr[2], tmpchr[3], tmpchr[0], tmpchr[1]};
            tmpdata[idx++] = tmptmpchr.toString();
        }
        Arrays.sort(tmpdata);

        dfs(0, n);

        return answer;
    }
}
