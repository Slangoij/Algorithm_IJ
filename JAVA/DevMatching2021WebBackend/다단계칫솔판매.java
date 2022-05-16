package DevMatching2021WebBackend;

import java.util.*;

public class 다단계칫솔판매 {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int[] answer = {};

        HashMap<String, String> parentMap = new HashMap<>();
        HashMap<String, Integer> memIdxMap = new HashMap<>();

        for (int i=0;i< enroll.length;i++){
            parentMap.put(enroll[i], referral[i]);
            memIdxMap.put(enroll[i], i);
        }

        for (int i=0;i< seller.length;i++){
            String nowMem = seller[i];

        }

        return answer;
    }
}
