
import java.util.Scanner;

public class LineByLine {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            String s = scanner.nextLine();
            if (s.equals("")) {
                break;
            }
            lineByline(s);
        }

        scanner.close();
    }

    public static void lineByline(String s) {
        String[] words = s.split(" ");

        for (String word : words) {
            System.out.println(word);
        }
    }
}
