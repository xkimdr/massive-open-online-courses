
import java.util.Scanner;

public class PrintThrice {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Write your program here
        String s = scanner.nextLine();

        scanner.close();

        printThrice(s);

    }

    public static void printThrice(String s) {
        System.out.println(s + s + s);
    }
}
