import java.util.ArrayList;

public class Stack {
    private ArrayList<String> items;

    public Stack() {
        this.items = new ArrayList<>();
    }

    public boolean isEmpty() {
        return this.items.size() == 0;
    }

    public void add(String value) {
        this.items.add(value);
    }

    public ArrayList<String> values() {
        return this.items;
    }

    public String take() {
        return this.items.remove(this.items.size() - 1);
    }
}
