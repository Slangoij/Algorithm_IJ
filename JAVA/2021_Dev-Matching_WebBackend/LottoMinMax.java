import java.util.*;

public class LottoMinMax{
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

        answer[1] = (tmpans > 5) ? 6:tmpans;
        tmpans -= numzero;
        answer[0] = (tmpans > 0) ? tmpans:1;
        
        return answer;
    }
	
	public static void main(String[] args){
		LottoMinMax lm = new LottoMinMax();
		
//		int[] lottos = {44, 1, 0, 0, 31, 25};
//		int[] win_nums = {31, 10, 45, 1, 6, 19};
		int[] lottos = {1,2,3,4,5,6};
		int[] win_nums = {7,8,9,10,11,12};
		
//		int[] tmpansss = lm.solution(lottos, win_nums);
		System.out.println(Arrays.toString(lm.solution(lottos, win_nums)));
//		System.out.println("foo");
	}
}