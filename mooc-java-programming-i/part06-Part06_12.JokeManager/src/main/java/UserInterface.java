import java.util.Scanner;

public class UserInterface {
    private JokeManager jokeManager;
    private Scanner scanner;

    public UserInterface(JokeManager jokeManager, Scanner scanner) {
        this.jokeManager = jokeManager;
        this.scanner = scanner;
    }

    public void start() {
        while (true) {
            String cmd = getCommand();

            switch (cmd) {
                case "X":
                    return;
                case "1":
                    this.add();
                    break;
                case "2":
                    this.draw();
                    break;
                case "3":
                    this.list();
                    break;
                default:
                    break;
            }
        }
    }

    private String getCommand() {
        System.out.println("Commands:");
        System.out.println(" 1 - add a joke");
        System.out.println(" 2 - draw a joke");
        System.out.println(" 3 - list jokes");
        System.out.println(" X - stop");

        return scanner.nextLine();
    }

    private void add() {
        System.out.println("Write the joke to be added:");
        String joke = this.scanner.nextLine();
        this.jokeManager.addJoke(joke);
    }

    private void draw() {
        System.out.println(this.jokeManager.drawJoke());
    }

    private void list() {
        this.jokeManager.printJokes();
    }
}
