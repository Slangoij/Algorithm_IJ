import Programmers.Kakaocode2017.단체사진찍기;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        단체사진찍기 solu = new 단체사진찍기();

        int n = 2;
//        String[] data = {"N~F=0", "R~T>2"};

//        System.out.println(solu.solution(
//                n, data
//        ));
        String[] data = {"N~F=<>0", "F~N>0", "F~N<0"};
//        Arrays.sort(data);
        char[] tmp = data[0].toCharArray();
        Arrays.sort(tmp);
        System.out.println(tmp);
//        System.out.println(Arrays.toString(data));
    }
}
