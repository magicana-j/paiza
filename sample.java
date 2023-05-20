import java.util.Scanner;

public class sample {
    private static int[] scanNumbers() {
        Scanner scan = new Scanner(System.in);
        String line = scan.nextLine();
        String[] values = line.split(" ", 0);
        int[] numbers = new int[values.length];
        for (int i = 0; i < values.length; i++) {
            try {
                numbers[i] = Integer.parseInt(values[i]);
            } catch (NumberFormatException ex) {
                return null;
            }
        }
        return numbers;
    }

    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}