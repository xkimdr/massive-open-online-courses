import java.util.ArrayList;
import java.util.Scanner;

public class Recipes {
    private ArrayList<Recipe> recipes;
    private Scanner scan;

    public Recipes(Scanner scanner) {
        this.scan = scanner;
        this.recipes = new ArrayList<>();
        this.populate();
    }

    private void populate() {
        while (this.scan.hasNextLine()) {
            String name = this.scan.nextLine();
            int time = Integer.valueOf(this.scan.nextLine());
            ArrayList<String> ingredients = new ArrayList<>();

            while (this.scan.hasNextLine()) {
                String ingredient = this.scan.nextLine();

                if (ingredient.length() == 0) {
                    break;
                }

                ingredients.add(ingredient);
            }

            this.recipes.add(new Recipe(name, time, ingredients));
        }
    }

    public void print() {
        System.out.println("Recipes: ");

        for (Recipe recipe : this.recipes) {
            System.out.println(recipe.toString());
        }
    }

    public void printByName(String name) {
        System.out.println("Recipes: ");

        for (Recipe recipe : this.recipes) {
            if (recipe.getName().contains(name)) {
                System.out.println(recipe.toString());
            }
        }
    }

    public void printByCookingTime(int time) {
        System.out.println("Recipes: ");

        for (Recipe recipe : this.recipes) {
            if (recipe.getTime() <= time) {
                System.out.println(recipe.toString());
            }
        }
    }

    public void printByIngredients(String ingredient) {
        System.out.println("Recipes: ");

        for (Recipe recipe : this.recipes) {
            if (recipe.containsIngredient(ingredient)) {
                System.out.println(recipe.toString());
            }
        }
    }
}
