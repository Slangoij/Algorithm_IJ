import Programmers.Kakaocode2017.단체사진찍기;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        단체사진찍기 solu = new 단체사진찍기();

        int n = 2;
//        String[] data = {"N~F=0", "R~T>2"};
        String[] data = {"M~C<2", "C~M>1"};
//        String[] data = {"N~F=0"};
        System.out.println(solu.solution(n, data));
    }
}
