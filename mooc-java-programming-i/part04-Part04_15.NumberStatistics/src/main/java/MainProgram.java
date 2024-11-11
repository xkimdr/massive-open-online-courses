
import java.util.Scanner;

public class MainProgram {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // you can write test code here
        // however, remove all unnecessary code when doing the final parts of the
        // exercise

        // In order for the tests to work, the objects must be created in the
        // correct order in the main program. First the object that tracks the total
        // sum, secondly the object that tracks the sum of even numbers,
        // and lastly the one that tracks the sum of odd numbers!
        int num = 0;

        Statistics t1 = new Statistics();
        Statistics t2 = new Statistics();
        Statistics t3 = new Statistics();

        System.out.println("Enter numbers:");

        while (true) {
            num = Integer.valueOf(scanner.nextLine());

            if (num == -1) {
                break;
            }

            t1.addNumber(num);

            if (num % 2 == 0) {
                t2.addNumber(num);
            } else {
                t3.addNumber(num);
            }
        }

        scanner.close();

        System.out.println("Sum: " + t1.sum());
        System.out.println("Sum of even numbers: " + t2.sum());
        System.out.println("Sum of odd numbers: " + t3.sum());
    }
}
