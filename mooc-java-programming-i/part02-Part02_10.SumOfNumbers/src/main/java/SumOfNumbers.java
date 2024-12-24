
import java.util.Scanner;

public class SumOfNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Give a number:");

        int value = 0;
        int sum = 0;

        while((value = Integer.valueOf(scanner.nextLine()))!= 0) {
            sum += value;

            System.out.println("Give a number:");
        }

        scanner.close();

        System.out.println("Sum of the numbers: " + sum);
    }
}
