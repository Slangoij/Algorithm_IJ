package Backjoon.Math;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 꼬마정민 {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Long> tmplst = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            tmplst.add(Long.parseLong(st.nextToken()));
        }

        System.out.println(tmplst.stream().mapToLong(Long::longValue).sum());
    }

    public static void main(String[] args) throws IOException {
        new 꼬마정민().solution();
    }
}
