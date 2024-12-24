
import java.util.Scanner;

public class Cubes {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            String s = scanner.nextLine();

            if (s.equals("end")) {
                break;
            }

            int x = Integer.valueOf(s);

            System.out.println((int) Math.pow(x, 3));
        }

        scanner.close();

    }
}
