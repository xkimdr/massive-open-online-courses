
import java.util.Scanner;

public class AgeOfTheOldest {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int age = 0;

        while (true) {
            String text = scanner.nextLine();

            if (text.equals("")) {
                break;
            }

            String[] array = text.split(",");

            int lage = Integer.valueOf(array[1]);

            if (lage > age) {
                age = lage;
            }
        }

        scanner.close();

        System.out.println("Age of the oldest: " + age);

    }
}
