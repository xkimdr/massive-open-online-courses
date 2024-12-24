
import java.util.Scanner;

public class NumberOfNegativeNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Give a number:");

        int value = 0;
        int count = 0;

        while ((value = Integer.valueOf(scanner.nextLine())) != 0) {
            if (value < 0) {
                ++count;
            }

            System.out.println("Give a number:");
        }

        scanner.close();

        System.out.println("Number of negative numbers: " + count);
    }
}
