package Programmers.KakaoBlind2019;

import java.util.*;

public class 실패율 {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int[] memStages = new int[N+2];
        Arrays.fill(memStages, 0);
        for (int i : stages) {
            memStages[i] += 1;
        }

        int totalparti = stages.length;
        double silperate;
        Map<Integer, Double> silpes = new HashMap<>();
        for (int i = 1; i < N+1; i++) {
            if (totalparti > 0){
                silperate = (double) memStages[i] / totalparti;
                silpes.put(i, silperate);
                totalparti -= memStages[i];
            }
            else {
                silpes.put(i, (double)0);
            }
        }

        List<Map.Entry<Integer, Double>> tosort =
                new ArrayList<Map.Entry<Integer, Double>>(silpes.entrySet());

        Collections.sort(tosort, new Comparator<Map.Entry<Integer, Double>>() {
            @Override
            public int compare(Map.Entry<Integer, Double> o1, Map.Entry<Integer, Double> o2) {
                return o2.getValue().compareTo(o1.getValue());
            }

        });
        int tmpi = 0;
        for (Map.Entry<Integer, Double> entry : tosort) {
            answer[tmpi] = entry.getKey();
            tmpi += 1;
        }

        return answer;
    }
}
