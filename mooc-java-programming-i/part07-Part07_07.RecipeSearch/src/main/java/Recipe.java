import java.util.ArrayList;

public class Recipe {
    private String name;
    private int time;
    private ArrayList<String> ingredients;

    public Recipe(String name, int time, ArrayList<String> ingredients) {
        this.name = name;
        this.time = time;
        this.ingredients = ingredients;
    }

    @Override
    public String toString() {
        return this.name + ", cooking time: " + this.time;
    }

    public String getName() {
        return this.name;
    }

    public int getTime() {
        return this.time;
    }

    public boolean containsIngredient(String ingredient) {
        for (String ing : this.ingredients) {
            if (ing.equals(ingredient)) {
                return true;
            }
        }

        return false;
    }
}
