
import java.util.Scanner;

public class AverageOfPositiveNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Give a number:");

        int value = 0;
        int count = 0;
        int sum = 0;

        while ((value = Integer.valueOf(scanner.nextLine())) != 0) {

            if (value > 0) {
                ++count;
                sum += value;
            }

            System.out.println("Give a number:");
        }

        scanner.close();

        if (sum == 0) {
            System.out.println("Cannot calculate the average");
            return;
        }

        double average = count == 0 ? 0 : (1.0 * sum) / count;

        System.out.println("Average of the numbers: " + average);

    }
}
