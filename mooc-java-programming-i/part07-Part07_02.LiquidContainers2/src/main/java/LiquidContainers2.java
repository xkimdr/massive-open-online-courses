
import java.util.Scanner;

public class LiquidContainers2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Container c1 = new Container();
        Container c2 = new Container();

        while (true) {
            System.out.println("First: " + c1.toString());
            System.out.println("Second:  " + c2.toString());

            String[] cmd = scan.nextLine().split(" ");

            if (cmd.length == 1) {
                if (cmd[0].equals("quit")) {
                    break;
                }
                continue;
            }

            String command = cmd[0];
            int amount = Integer.valueOf(cmd[1]);

            if (command.equals("add")) {
                c1.add(amount);
            } else if (command.equals("move")) {
                if (c1.contains() - amount < 0) {
                    c2.add(c1.contains());
                    c1.remove(c1.contains());
                } else {
                    c1.remove(amount);
                    c2.add(amount);
                }
            } else if (command.equals("remove")) {
                c2.remove(amount);
            }
        }

        scan.close();
    }

}
