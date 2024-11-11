
import java.util.Scanner;

public class Message {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Write a message:");
        // Write your program here
        String s = scanner.nextLine();
        scanner.close();

        System.out.println(s);
    }
}
