import java.util.Scanner;

public class UI {
    Container c1;
    Container c2;
    Scanner scan;

    public UI(Scanner scanner) {
        this.c1 = new Container();
        this.c2 = new Container();
        this.scan = scanner;
    }

    public void start() {
        while (true) {
            this.printContainers();

            String input = scan.nextLine();
            if (input.equals("quit")) {
                break;
            }

            String array[] = input.split(" ");
            String cmd = array[0];
            int value = Integer.valueOf(array[1]);

            switch (cmd) {
                case "add":
                    this.add(value);
                    break;
                case "move":
                    this.move(value);
                    break;
                case "remove":
                    this.remove(value);
                    break;
                default:
                    break;
            }

            System.out.println();

        }
    }

    private void printContainers() {
        System.out.println("First: " + c1);
        System.out.println("Second: " + c2);
    }

    private void add(int value) {
        this.c1.add(value);
    }

    private void move(int value) {
        if (value > this.c1.contains()) {
            this.c2.add(this.c1.contains());
            this.c1.remove(this.c1.contains());
        } else {
            this.c1.remove(value);
            this.c2.add(value);
        }
    }

    private void remove(int value) {
        this.c2.remove(value);
    }

}
