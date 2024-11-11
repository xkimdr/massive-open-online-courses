import java.util.Scanner;

public class UI {
    private Recipes recipes;
    private Scanner scanner;

    public UI(Recipes recipes, Scanner scanner) {
        this.recipes = recipes;
        this.scanner = scanner;
    }

    public void start() {
        System.out.println("list - lists the recipes\n" + //
                "stop - stops the program\n" + //
                "find name - searches recipes by name\n" + //
                "find cooking time - searches recipes by cooking time\n" + //
                "find ingredient - searches recipes by ingredient");

        while (true) {
            System.out.println();

            String cmd = getCommand();

            switch (cmd) {
                case "stop":
                    return;
                case "list":
                    this.list();
                    break;
                case "find name":
                    this.findName();
                    break;
                case "find cooking time":
                    this.findCookingTime();
                    break;
                case "find ingredient":
                    this.findIngredient();
                default:
                    break;
            }
        }
    }

    private String getCommand() {
        System.out.print("Enter command: ");
        return this.scanner.nextLine();
    }

    private void list() {
        System.out.println();
        this.recipes.print();
    }

    private void findName() {
        System.out.print("Searched word: ");
        String name = this.scanner.nextLine();

        System.out.println();
        this.recipes.printByName(name);
    }

    private void findCookingTime() {
        System.out.print("Max cooking time: ");
        int time = Integer.valueOf(this.scanner.nextLine());

        System.out.println();
        this.recipes.printByCookingTime(time);
    }

    private void findIngredient() {
        System.out.print("Ingredient: ");
        String name = this.scanner.nextLine();

        System.out.println();
        this.recipes.printByIngredients(name);
    }
}
