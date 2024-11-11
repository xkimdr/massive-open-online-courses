
import java.util.ArrayList;
import java.util.Scanner;
import java.util.List;

public class AverageOfSelectedNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // toteuta ohjelmasi tänne
        List<String> values = new ArrayList<>();

        System.out.println("Input numbers, type \"end\" to stop.");

        while (true) {
            String s = scanner.nextLine();

            if (s.equals("end")) {
                break;
            }

            values.add(s);
        }

        System.out.println("Print the average of the negative numbers or the positive numbers? (n/p)");

        String s = scanner.nextLine();
        scanner.close();

        double avg = 0;

        if (s.equals("n")) {
            avg = values.stream().mapToInt(x -> Integer.valueOf(x)).filter(y -> y < 0).average().getAsDouble();
            System.out.println("Average of the negative numbers: " + avg);
        } else if (s.equals("p")) {
            avg = values.stream().mapToInt(x -> Integer.valueOf(x)).filter(y -> y > 0).average().getAsDouble();
            System.out.println("Average of the positive numbers: " + avg);
        }

    }
}
