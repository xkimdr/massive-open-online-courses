
import java.util.Scanner;

public class LargerThanOrEqualTo {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Give the first number:");
        int x = Integer.valueOf(scan.nextLine());

        System.out.println("Give the second number:");
        int y = Integer.valueOf(scan.nextLine());

        scan.close();

        if (x == y) {
            System.out.println("The numbers are equal!");
        } else {
            System.out.print("Greater number is: ");
            if (x > y) {
                System.out.println(x);
            } else {
                System.out.println(y);
            }
        }
    }
}
