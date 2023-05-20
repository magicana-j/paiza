import java.util.*;

public class Sample2 {
    public static void main(String[] args) {
        // 自分の得意な言語で
        // Let's チャレンジ！！
        Scanner sc = new Scanner(System.in);

        final int N = sc.nextInt();
        String dummy;
        dummy = sc.nextLine();

        String[] line = new String[N];
        for (int i = 0; i < N; i++) {
            line[i] = sc.nextLine();
        }
        for (int i = 0; i < N; i++) {
            System.out.println(line[i]);
        }
    }
}