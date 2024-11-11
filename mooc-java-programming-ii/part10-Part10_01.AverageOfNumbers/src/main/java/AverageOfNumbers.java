
import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;

public class AverageOfNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Write your program here
        List<String> values = new ArrayList<>();

        System.out.println("Input numbers, type \"end\" to stop.");

        while (true) {
            String s = scanner.nextLine();

            if (s.equals("end")) {
                break;
            }

            values.add(s);
        }

        scanner.close();

        double avg = 0;

        if (!values.isEmpty()) {
            avg = values.stream().mapToInt(s -> Integer.valueOf(s)).average().getAsDouble();
        }

        System.out.println("average of the numbers: " + avg);
    }
}
