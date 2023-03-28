package Programmers;

import java.util.*;

public class 위장 {
    public int solution(String[][] clothes) {
        int answer = 1;

        HashMap<String, ArrayList<String>> closet = new HashMap<>();
        for (String[] item : clothes) {
            if (closet.containsKey(item[1])) {
                ArrayList<String> tmpList = closet.get(item[1]);
                tmpList.add(item[0]);
                closet.put(item[1], tmpList);
            } else {
                ArrayList<String> tmpList = new ArrayList<>(Arrays.asList(item[0]));
                closet.put(item[1], tmpList);
            }
        }

        for (Map.Entry<String, ArrayList<String>> entry : closet.entrySet()) {
            answer *= entry.getValue().size() + 1;
        }

        return answer - 1;
    }
}
