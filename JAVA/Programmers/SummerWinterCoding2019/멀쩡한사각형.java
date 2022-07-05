package Programmers.SummerWinterCoding2019;

import java.math.BigInteger;

public class 멀쩡한사각형 {
    public long solution(int w, int h) {
        long answer = w * h;
        int gcd = BigInteger.valueOf(w).gcd(BigInteger.valueOf(h)).intValue();
        int min = Math.min(w, h);
        int max = Math.max(w, h);
        double grad = (double) max / min;
        int tosubstract = 0;
        double tmp = 0;
        for (int i = 1; i < min / gcd + 1; i++) {
            tosubstract += Math.ceil(tmp + grad) - Math.floor(tmp);
            tmp += grad;
        }

        return answer - (long) (tosubstract * gcd);
    }
}
