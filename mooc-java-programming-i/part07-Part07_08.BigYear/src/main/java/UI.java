import java.util.Scanner;

public class UI {
    private Birds birds;
    private Scanner scanner;

    public UI(Scanner scanner) {
        this.birds = new Birds();
        this.scanner = scanner;
    }

    public void start() {
        while (true) {
            String cmd = getCommand();

            switch (cmd) {
                case "Quit":
                    return;
                case "Add":
                    this.add();
                    break;
                case "Observation":
                    this.observation();
                    break;
                case "One":
                    this.one();
                    break;
                case "All":
                    this.all();
                    break;
                default:
                    break;
            }
        }
    }

    private String getCommand() {
        System.out.print("? ");
        return this.scanner.nextLine();
    }

    private void add() {
        System.out.print("Name: ");
        String name = this.scanner.nextLine();

        System.out.print("Name in Latin: ");
        String lname = this.scanner.nextLine();

        this.birds.add(name, lname);
    }

    private void observation() {
        System.out.print("Bird? ");
        String name = this.scanner.nextLine();

        if (!this.birds.observation(name)) {
            System.out.println("Not a bird!");
        }
    }

    private void one() {
        System.out.print("Bird? ");
        String name = this.scanner.nextLine();

        this.birds.prineOne(name);
    }

    private void all() {
        this.birds.printAll();
    }
}
