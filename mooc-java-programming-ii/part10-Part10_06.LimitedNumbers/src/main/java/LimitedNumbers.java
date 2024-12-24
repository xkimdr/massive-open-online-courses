
import java.util.ArrayList;
import java.util.Scanner;

public class LimitedNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        ArrayList<Integer> nums = new ArrayList<>();

        while (true) {
            int x = Integer.valueOf(scanner.nextLine());

            if (x < 0) {
                break;
            }

            nums.add(x);
        }

        scanner.close();

        nums.stream().filter(x -> x >= 1 && x <= 5).forEach(x -> System.out.println(x));

    }
}
