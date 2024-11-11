
import java.util.Scanner;

public class LiquidContainers {

    public static void main(String[] args) {
        int c1 = 0;
        int c2 = 0;

        Scanner scan = new Scanner(System.in);

        while (true) {
            System.out.println("First: " + c1 + "/100");
            System.out.println("Second:  " + c2 + "/100");

            String[] cmd = scan.nextLine().split(" ");

            if (cmd.length == 1) {
                if (cmd[0].equals("quit")) {
                    break;
                }
                continue;
            }

            String command = cmd[0];
            int amount = Integer.valueOf(cmd[1]);

            if (amount < 0) {
                continue;
            }

            if (command.equals("add")) {
                int newAmount = c1 + amount;

                if (newAmount > 100) {
                    c1 = 100;
                    continue;
                }

                c1 = newAmount;
            } else if (command.equals("move")) {
                int newAmount = c1 - amount;

                if (newAmount < 0) {
                    c2 += c1;
                    c1 = 0;
                } else {
                    c1 = newAmount;
                    c2 += amount;
                }

                if (c2 > 100) {
                    c2 = 100;
                }
            } else if (command.equals("remove")) {
                int newAmount = c2 - amount;

                if (newAmount < 0) {
                    c2 = 0;
                    continue;
                }

                c2 = newAmount;
            }
        }

        scan.close();
    }

}
