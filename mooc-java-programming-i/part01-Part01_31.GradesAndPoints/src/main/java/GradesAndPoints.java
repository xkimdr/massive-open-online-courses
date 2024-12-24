
import java.util.Scanner;

public class GradesAndPoints {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.println("Give points [0-100]:");
        int x = Integer.valueOf(scan.nextLine());

        scan.close();

        System.out.print("Grade: ");
        if (x > 100) {
            System.out.println("incredible!");
        } else if (x >= 90) {
            System.out.println("5");
        } else if (x >= 80) {
            System.out.println("4");
        } else if (x >= 70) {
            System.out.println("3");
        } else if (x >= 60) {
            System.out.println("2");
        } else if (x >= 50) {
            System.out.println("1");
        } else if (x >= 0) {
            System.out.println("failed");
        } else {
            System.out.println("impossible!");
        }

    }
}
