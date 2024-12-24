
import java.util.Scanner;

public class AbsoluteValue {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int x = Integer.valueOf(scanner.nextLine());

        scanner.close();

        int absValue = x;
        if (x < 0) {
            absValue = -1 * x;
        }

        System.out.println(absValue);

    }
}
