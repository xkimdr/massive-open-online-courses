import java.util.Scanner;

public class TextUI {
    private Scanner scan;
    private SimpleDictionary dict;

    public TextUI(Scanner scanner, SimpleDictionary simpleDictionary) {
        this.scan = scanner;
        this.dict = simpleDictionary;
    }

    public void start() {
        while (true) {
            String cmd = this.getCommand();

            switch (cmd) {
                case "add":
                    this.add();
                    break;
                case "search":
                    this.search();
                    break;
                case "end":
                    this.end();
                    return;
                default:
                    this.unkown();
                    break;
            }
        }
    }

    private String getCommand() {
        System.out.print("Command: ");
        return this.scan.nextLine();
    }

    private void add() {
        System.out.print("Word: ");
        String word = this.scan.nextLine();

        System.out.print("Translation: ");
        String translation = this.scan.nextLine();

        dict.add(word, translation);
    }

    private void search() {
        System.out.print("To be translated: ");
        String word = this.scan.nextLine();

        String translation = dict.translate(word);

        if (translation == null) {
            System.out.println("Word " + word + " was not found");
        } else {
            System.out.println("Translation: " + translation);
        }
    }

    private void end() {
        System.out.println("Bye bye!");
    }

    private void unkown() {
        System.out.println("Unknown command");
    }
}
