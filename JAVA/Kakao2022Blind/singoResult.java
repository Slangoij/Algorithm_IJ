package Kakao2022Blind;

import java.util.*;
import java.util.Map.Entry;

public class singoResult {
    public int[] solution(String[] id_list, String[] report, int k) {
        List<String> lst = Arrays.asList(report);
        Set<String> set = new HashSet<String>(lst);
        List<String> newList = new ArrayList<String>(set);
        HashMap<String, ArrayList<String>> map = new HashMap<>();
        for (String str: newList) {
        	String[] splitstr = str.split(" ");
        	ArrayList<String> tmp = new ArrayList<>(Arrays.asList());
    		ArrayList<String> tmplst = map.getOrDefault(splitstr[1], tmp);
    		tmplst.add(splitstr[0]);
    		map.put(splitstr[1], tmplst);
        }

        HashMap<String, Integer> reportmap = new HashMap<>();
        for (Entry<String, ArrayList<String>> entryset : map.entrySet()) {
        	ArrayList<String> nowlst = entryset.getValue();
        	int nowsize = nowlst.size();
        	if (nowsize >= k) {
        		for (String nowkey:nowlst) {
        			reportmap.put(nowkey, reportmap.getOrDefault(nowkey, 0) + 1);
        		}
        	}
        }
        
        ArrayList<Integer> anslist = new ArrayList<>();
        for (String id:id_list) {
        	anslist.add(reportmap.getOrDefault(id, 0));
        }
        
        int[] answer = new int[id_list.length];
        for (int i=0;i<id_list.length;i++) {
        	answer[i] = anslist.get(i);
        }
        
        return answer;
    }
    
    public static void main(String[] args) {
    	singoResult gu = new singoResult();
    	
    	String[] id_list = {"muzi", "frodo", "apeach", "neo"};
    	String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
    	int k = 2;
    	
    	System.out.println(gu.solution(id_list, report, k));
    }
}