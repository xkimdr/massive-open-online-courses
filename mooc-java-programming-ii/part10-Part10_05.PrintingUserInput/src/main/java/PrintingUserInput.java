
import java.util.ArrayList;
import java.util.Scanner;

public class PrintingUserInput {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> strings = new ArrayList<>();

        while (true) {
            String s = scanner.nextLine();

            if (s.isEmpty()) {
                break;
            }

            strings.add(s);
        }

        strings.stream().forEach(x -> System.out.println(x));
    }
}
