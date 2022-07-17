package Backjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> tmplst = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            tmplst.add(Integer.parseInt(st.nextToken()));
        }

        int v = Integer.parseInt(br.readLine());
        System.out.println(Collections.frequency(tmplst, v));
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}
