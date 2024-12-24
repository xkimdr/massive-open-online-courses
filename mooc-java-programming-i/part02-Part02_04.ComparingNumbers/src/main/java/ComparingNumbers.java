
import java.util.Scanner;

public class ComparingNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int x = Integer.valueOf(scanner.nextLine());
        int y = Integer.valueOf(scanner.nextLine());

        scanner.close();

        System.out.print(x + " is ");
        if (x > y) {
            System.out.print("greater than ");
        } else if (x < y) {
            System.out.print("smaller than ");
        } else {
            System.out.print("equal to ");
        }
        System.out.println(y + ".");

    }
}
