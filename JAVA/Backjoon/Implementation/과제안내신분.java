package Backjoon.Implementation;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class 과제안내신분 {
    public void solution() throws IOException {
        List<Integer> stdlst = new ArrayList<>();
        for (int i = 1; i <= 30; i++) {
            stdlst.add(i);
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 28; i++) {
            stdlst.remove(Integer.valueOf(Integer.parseInt(br.readLine())));
        }
        System.out.println(Collections.min(stdlst));
        System.out.println(Collections.max(stdlst));
    }

    public static void main(String[] args) throws IOException {
        new 과제안내신분().solution();
    }
}