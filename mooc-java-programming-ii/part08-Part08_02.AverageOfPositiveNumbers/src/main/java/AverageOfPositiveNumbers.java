
import java.util.Scanner;

public class AverageOfPositiveNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;
        int count = 0;

        while (true) {
            int x = Integer.valueOf(scanner.nextLine());

            if (x == 0) {
                break;
            }

            if (x > 0) {
                sum += x;
                ++count;
            }
        }

        scanner.close();

        if (count == 0) {
            System.out.println("Cannot calculate the average");
            return;
        }

        System.out.println((double) sum / count);
    }
}
