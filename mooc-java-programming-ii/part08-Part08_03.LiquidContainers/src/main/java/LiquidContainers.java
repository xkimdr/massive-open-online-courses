
import java.util.Scanner;

public class LiquidContainers {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int c1 = 0;
        int c2 = 0;

        while (true) {
            System.out.println("First: " + c1 + "/100");
            System.out.println("Second: " + c2 + "/100");

            String input = scan.nextLine();
            if (input.equals("quit")) {
                break;
            }

            String array[] = input.split(" ");
            String cmd = array[0];
            int value = Integer.valueOf(array[1]);

            if (value < 0) {
                continue;
            }

            if (cmd.equals("add")) {
                if (c1 + value > 100) {
                    c1 = 100;
                } else {
                    c1 += value;
                }
            } else if (cmd.equals("move")) {
                if (value > c1) {
                    c2 += c1;
                    c1 = 0;
                } else {
                    c2 += value;
                    c1 -= value;
                }

                if (c2 > 100) {
                    c2 = 100;
                }
            } else if (cmd.equals("remove")) {
                if (value > c2) {
                    c2 = 0;
                } else {
                    c2 -= value;
                }

            }

            System.out.println();
        }

        scan.close();
    }

}
