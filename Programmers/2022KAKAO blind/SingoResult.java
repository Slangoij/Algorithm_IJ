import java.util.*;

class SingoResult{
    public static void main(String[] args) {

        solution();
    }

    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = {};

        HashMap<String, ArrayList<String>> map = new HashMap<>();
        foreach(String str : report)
        {
            String[] splstr = str.split();
            if (map.get(splstr[1]) == null)
            {
                ArrayList<String> tmparr = new ArrayList<String>(Arrays.asList(splstr[0]));
                map.put(splstr[1], tmparr);
            }
            else
            {
                map.put(splstr[1], map.get(splstr[1]).add(splstr[0]));
            }
        }
        
        return answer;
    }
}

