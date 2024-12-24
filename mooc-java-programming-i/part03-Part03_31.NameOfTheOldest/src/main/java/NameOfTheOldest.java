
import java.util.Scanner;

public class NameOfTheOldest {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int age = 0;
        String name = "";

        while (true) {
            String text = scanner.nextLine();

            if (text.equals("")) {
                break;
            }

            String[] array = text.split(",");

            int lage = Integer.valueOf(array[1]);

            if (lage > age) {
                age = lage;
                name = array[0];
            }
        }

        scanner.close();

        System.out.println("Name of the oldest: " + name);
    }
}
