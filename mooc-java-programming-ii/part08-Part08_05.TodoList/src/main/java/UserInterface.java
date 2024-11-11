import java.util.Scanner;

public class UserInterface {
    private TodoList todo;
    private Scanner scan;

    public UserInterface(TodoList list, Scanner scanner) {
        this.todo = list;
        this.scan = scanner;
    }

    public void start() {
        while (true) {
            String cmd = getCommand();

            switch (cmd) {
                case "stop":
                    return;
                case "add":
                    this.add();
                    break;
                case "list":
                    this.list();
                    break;
                case "remove":
                    this.remove();
                    break;

                default:
                    break;
            }
        }
    }

    private String getCommand() {
        System.out.print("Command: ");
        return scan.nextLine();
    }

    private void add() {
        System.out.print("To add: ");
        this.todo.add(scan.nextLine());
    }

    private void list() {
        this.todo.print();
    }

    private void remove() {
        System.out.print("Which one is removed? ");
        this.todo.remove(Integer.valueOf(scan.nextLine()));
    }
}
