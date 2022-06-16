package Programmers;

import java.util.ArrayList;

public class 조이스틱 {
    ArrayList<Integer> perm = new ArrayList<>();
    int[] arr;
    int len;
    int answer = 0;
    int posans = 100;

    static void swap(int[] arr, int depth, int i) {
        int tmp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = tmp;
    }

    public void perm(int now, int trg) {
        if (now == trg) {
            int tmp = 0;
            int tmpdist;
            int tmpans = 0;
            for (int i = 0; i < arr.length; i++) {
                tmpdist = Math.abs(tmp - arr[i]);
                tmpans += Math.min(Math.abs(len - tmpdist), tmpdist);
                tmp = arr[i];
            }
            posans = Math.min(posans, tmpans);
        }

        for (int i = now; i < trg; i++) {
            swap(arr, now, i);
            perm(now+1, trg);
            swap(arr, now, i);
        }
    }

    public int getDistFromA(char chr) {
        int a = (int) 'Z' + 1;
        int b = (int) 'A';
        return Math.min(Math.abs(a - (int) chr), Math.abs((int) chr - b));
    }

    public int solution(String name) {
        int cnt = 0;
        len = name.length();

        for (int i = 0; i < name.length(); i++) {
            answer += getDistFromA(name.charAt(i));
            if (i != 0 && name.charAt(i) != 'A') {
                cnt++;
            }
        }
        arr = new int[cnt];
        cnt = 0;
        for (int i = 1; i < name.length(); i++) {
            if (name.charAt(i) != 'A') {
                arr[cnt] = i;
                cnt++;
            }
        }

        perm(0, cnt);

        return answer + posans;

//        while (idx == nxtidx) {
//            for (int i = 1; i < (name.length() / 2) + 1; i++) {
//                nxtidx = (idx + i) % name.length();
//                if (name.charAt(nxtidx) != 'A' && !vstd[nxtidx]) {
//                    vstd[nxtidx] = true;
//                    idx = nxtidx;
//                    break;
//                } else {
//                    nxtidx = (idx - i + name.length()) % name.length();
//                    if (name.charAt(nxtidx) != 'A' && !vstd[nxtidx]) {
//                        vstd[nxtidx] = true;
//                        idx = nxtidx;
//                        break;
//                    }
//                }
//            }
//        }

    }
//        for (int i = 0; i < name.length(); i++) {
//            answer += getDistFromA(name.charAt(i));
//            if (name.charAt(i) != 'A' && i != 0) {
//                cnt++;
//                maxdist = Math.max(maxdist, Math.min(name.length() - i, i));
//            }
//        }
//
//        return answer + Math.max(cnt, maxdist);
//    }
}
