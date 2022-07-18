package Backjoon.Implementation;

import java.io.IOException;
import java.time.LocalDate;
import java.time.ZoneId;

public class 오늘날짜 {
    public void solution() throws IOException {
        LocalDate now = LocalDate.now();
        LocalDate seoulNow = LocalDate.now(ZoneId.of("Asia/Seoul"));
        System.out.println(seoulNow);
    }

    public static void main(String[] args) throws IOException {
        new 오늘날짜().solution();
    }
}
