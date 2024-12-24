
import java.util.Scanner;

public class OnlyPositives {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int x = 1;
        while (x != 0) {
            System.out.println("Give a number:");
            x = Integer.valueOf(scanner.nextLine());

            if (x > 0) {
                System.out.println(x * x);
            } else if (x < 0) {
                System.out.println("Unsuitable number");
            }
        }

        scanner.close();
    }
}
