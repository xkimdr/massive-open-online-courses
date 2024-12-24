
import java.util.Scanner;

public class AreWeThereYet {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int x = 0;
        while (x != 4) {
            System.out.println("Give a number:");
            x = Integer.valueOf(scanner.nextLine());
        }

        scanner.close();
    }
}
