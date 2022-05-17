package Programmers.DevMatching2021WebBackend;

import java.util.*;

public class 로또의최고순위와최저순위 {
    public int[] solution(int[] lottos, int[] win_nums) {
    	int tmpans = 7;
    	int numzero = 0;
        int[] answer = {0, 0};
        
        ArrayList<Integer> lotarr = new ArrayList<>();
        for (int i:lottos) {
        	lotarr.add(i);
        }
        ArrayList<Integer> winarr = new ArrayList<>();
        for (int i:win_nums) {
        	winarr.add(i);
        }
        Collections.sort(lotarr);
        Collections.sort(winarr);
//        winarr.sort(Comparator.naturalOrder());        
        
        for (int nownum:lotarr) {
        	if (nownum > 0) {
        		if (winarr.indexOf(nownum) >= 0) {
            		tmpans--;
        		}
        	}
        	else {
        		numzero++;
        	}
        }
        tmpans = (tmpans > 5) ? 6:tmpans;
        answer[1] = tmpans; 
        tmpans -= numzero;
        answer[0] = (tmpans > 0) ? tmpans:1;
        
        return answer;
    }
}