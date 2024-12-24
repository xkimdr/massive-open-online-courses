import java.nio.file.Paths;
import java.util.Scanner;

public class RecipeSearch {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("File to read: ");
        String file = scan.nextLine();

        System.out.println();

        try (Scanner scanner = new Scanner(Paths.get(file))) {
            UI ui = new UI(new Recipes(scanner), scan);
            ui.start();
        } catch (Exception e) {
            System.out.println(e);
        }
    }

}
