import java.util.Scanner;

public class UserInterface {
    private Scanner scan;
    private TodoList todo;

    public UserInterface(TodoList todoList, Scanner scanner) {
        this.scan = scanner;
        this.todo = todoList;
    }

    public void start() {
        while (true) {
            String cmd = this.getCommand();

            switch (cmd) {
                case "stop":
                    return;
                case "add":
                    this.add();
                    break;
                case "remove":
                    this.remove();
                    break;
                case "list":
                    this.list();
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

    private void remove() {
        System.out.print("Which one is removed? ");
        this.todo.remove(Integer.valueOf(scan.nextLine()));
    }

    private void list() {
        this.todo.print();
    }
}
